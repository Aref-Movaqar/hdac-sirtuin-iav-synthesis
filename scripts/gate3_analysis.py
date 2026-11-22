#!/usr/bin/env python3
"""
Gate 3. Does PA-X cut preferentially in terminal exons?

Data: GEO GSE207253, transcriptome-wide PA-X cut sites mapped by 5' RACE-seq in
A549 cells (Gaucherand & Gaglia, Nat Microbiol 2023). Annotation: UCSC refGene,
hg38, confirmed as the build by build_check.py.

PRIMARY ANALYSIS, within transcript. For each transcript carrying at least one
cut site, the question is which of its own exons the cut fell in. Conditional
(stratified) logistic regression with transcript as the stratum, outcome = exon
contains a cut, predictors = terminal-exon status and log exon length.

Stratifying by transcript removes every transcript-level confounder by
construction: expression, transcript length, GC content, 3' UTR length, gene
family and detection bias are all constant within a stratum and cannot
contribute. Exon length is the one covariate that must still be modelled,
because terminal exons are systematically the longest. Its coefficient is
estimated rather than fixed at 1, so the model answers whether terminal
position adds anything beyond length.

SECONDARY ANALYSIS, between transcript. Logistic regression over all annotated
transcripts of whether a transcript carries any cut site, with terminal-exon
length, 3' UTR length, total transcript length and exon count as predictors.
This is the question the Gate 3 brief asked for. It is reported second because
it is the weaker design: it cannot control baseline expression without external
data, and detection of a cut site is expression-dependent.

Usage: python3 -I gate3_analysis.py raw/ [--cuts shared|concatenated]
"""
import collections, gzip, math, sys
import numpy as np
import pandas as pd

RG = dict(name=1, chrom=2, strand=3, txStart=4, txEnd=5, cdsStart=6, cdsEnd=7,
          exonStarts=9, exonEnds=10, name2=12)


# ------------------------------------------------------------------ loading
def load_refgene(path):
    tx = []
    with gzip.open(path, "rt") as fh:
        for line in fh:
            f = line.rstrip("\n").split("\t")
            if len(f) < 13:
                continue
            try:
                starts = [int(x) for x in f[RG["exonStarts"]].rstrip(",").split(",")]
                ends = [int(x) for x in f[RG["exonEnds"]].rstrip(",").split(",")]
            except ValueError:
                continue
            if len(starts) != len(ends):
                continue
            tx.append(dict(name=f[RG["name"]], chrom=f[RG["chrom"]], strand=f[RG["strand"]],
                           txStart=int(f[RG["txStart"]]), txEnd=int(f[RG["txEnd"]]),
                           cdsStart=int(f[RG["cdsStart"]]), cdsEnd=int(f[RG["cdsEnd"]]),
                           starts=starts, ends=ends, gene=f[RG["name2"]]))
    return tx


def load_cuts(path):
    out = []
    with gzip.open(path, "rt") as fh:
        hdr = fh.readline().rstrip("\n").split("\t")
        i = {k: n for n, k in enumerate(hdr)}
        for line in fh:
            f = line.rstrip("\n").split("\t")
            out.append(dict(chrom=f[i["Chromosome"]], strand=f[i["Strand"]],
                            pos=int(f[i["Cut_location"]]), gene=f[i["Gene_name"]],
                            seq=f[i["Sequence_around_cut_site"]]))
    return out


# ------------------------------------------------------------------ geometry
def exon_table(t):
    """Exons in transcription order, with region and terminal flags."""
    n = len(t["starts"])
    idx = range(n) if t["strand"] == "+" else range(n - 1, -1, -1)
    rows = []
    for k, j in enumerate(idx):
        s, e = t["starts"][j], t["ends"][j]
        rows.append(dict(exon_order=k + 1, gstart=s, gend=e, length=e - s,
                         is_first=(k == 0), is_terminal=(k == n - 1)))
    return rows


def region_of(t, pos):
    """5UTR / CDS / 3UTR for a genomic position, in transcript orientation."""
    cs, ce = t["cdsStart"], t["cdsEnd"]
    if cs == ce:
        return "noncoding"
    if cs <= pos < ce:
        return "CDS"
    if t["strand"] == "+":
        return "5UTR" if pos < cs else "3UTR"
    return "3UTR" if pos < cs else "5UTR"


def junction_positions(t):
    """Internal exon boundaries (genomic), i.e. all but the outer two ends."""
    js = []
    for j in range(len(t["starts"])):
        if j > 0:
            js.append(t["starts"][j])
        if j < len(t["starts"]) - 1:
            js.append(t["ends"][j])
    return sorted(js)


def exonic_length(t):
    return sum(e - s for s, e in zip(t["starts"], t["ends"]))


def utr3_length(t):
    if t["cdsStart"] == t["cdsEnd"]:
        return np.nan
    tot = 0
    for s, e in zip(t["starts"], t["ends"]):
        if t["strand"] == "+":
            lo, hi = max(s, t["cdsEnd"]), e
        else:
            lo, hi = s, min(e, t["cdsStart"])
        if hi > lo:
            tot += hi - lo
    return tot


def terminal_exon_length(t):
    return (t["ends"][-1] - t["starts"][-1]) if t["strand"] == "+" \
        else (t["ends"][0] - t["starts"][0])


# ------------------------------------------------------------------ main
def main():
    d = (sys.argv[1] if len(sys.argv) > 1 else "raw").rstrip("/")
    which = "concatenated"
    if "--cuts" in sys.argv:
        which = sys.argv[sys.argv.index("--cuts") + 1]
    print(f"=== Gate 3: PA-X cut sites vs exon architecture ({which} set) ===\n")

    tx = load_refgene(f"{d}/refGene_hg38.txt.gz")
    cuts = load_cuts(f"{d}/PA-X_{which}_cut_sites.txt.gz")
    print(f"transcripts: {len(tx)}   cut sites: {len(cuts)}")

    # index transcripts by chrom for assignment
    by_chrom = collections.defaultdict(list)
    for t in tx:
        by_chrom[t["chrom"]].append(t)

    # ---- assign each cut to a transcript -----------------------------------
    # Candidates: same chrom and strand, cut inside an exon. Prefer the
    # transcript whose gene symbol matches the file's own annotation, then the
    # one with the most exons, then the longest exonic length. Recording the
    # number of candidates lets us report how often the choice is ambiguous.
    assigned, unassigned, ncand = [], 0, []
    for c in cuts:
        cands = []
        for t in by_chrom.get(c["chrom"], []):
            if t["strand"] != c["strand"]:
                continue
            if not (t["txStart"] <= c["pos"] <= t["txEnd"]):
                continue
            for s, e in zip(t["starts"], t["ends"]):
                if s <= c["pos"] < e:
                    cands.append(t)
                    break
        if not cands:
            unassigned += 1
            continue
        ncand.append(len(cands))
        named = [t for t in cands if t["gene"] == c["gene"]]
        pool = named or cands
        best = max(pool, key=lambda t: (len(t["starts"]), exonic_length(t)))
        assigned.append((c, best))
    print(f"cuts assigned to an exon of an annotated transcript: {len(assigned)}"
          f"   unassigned (intronic/unannotated): {unassigned}")
    print(f"median candidate transcripts per cut: {int(np.median(ncand)) if ncand else 0}")

    # ---- cut-level description --------------------------------------------
    recs = []
    for c, t in assigned:
        ex = exon_table(t)
        hit = next(e for e in ex if e["gstart"] <= c["pos"] < e["gend"])
        js = junction_positions(t)
        dj = min((abs(c["pos"] - j) for j in js), default=np.nan)
        # signed distance to the nearest DOWNSTREAM junction in transcript sense
        recs.append(dict(gene=t["gene"], tx=t["name"], n_exons=len(ex),
                         exon_order=hit["exon_order"], is_terminal=hit["is_terminal"],
                         is_first=hit["is_first"], exon_len=hit["length"],
                         region=region_of(t, c["pos"]), dist_junction=dj,
                         gc_local=(c["seq"].count("G") + c["seq"].count("C")) / len(c["seq"]),
                         term_exon_len=terminal_exon_length(t),
                         utr3_len=utr3_length(t), tx_exonic_len=exonic_length(t)))
    cut = pd.DataFrame(recs)
    print(f"\n--- where the cuts fall (n={len(cut)}) ---")
    print(f"  in the terminal exon:            {cut.is_terminal.sum()} "
          f"({100*cut.is_terminal.mean():.1f}%)")
    print(f"  in the first exon:               {cut.is_first.sum()} "
          f"({100*cut.is_first.mean():.1f}%)")
    print(f"  single-exon transcripts:         {(cut.n_exons==1).sum()}")
    print(f"  region: " + ", ".join(f"{k} {v}" for k, v in cut.region.value_counts().items()))
    print(f"  median distance to nearest junction: {cut.dist_junction.median():.0f} nt")
    print(f"  mean local GC (99-nt context):   {cut.gc_local.mean():.3f}")

    # ---- PRIMARY: within-transcript conditional logistic -------------------
    # Build the exon-level design for transcripts carrying >=1 cut, excluding
    # single-exon transcripts (no within-stratum contrast possible).
    hits = collections.Counter((t["name"], e["exon_order"])
                               for c, t in assigned
                               for e in exon_table(t)
                               if e["gstart"] <= c["pos"] < e["gend"])
    used_tx = {t["name"]: t for c, t in assigned}
    rows = []
    for name, t in used_tx.items():
        ex = exon_table(t)
        if len(ex) < 2:
            continue
        for e in ex:
            rows.append(dict(tx=name, gene=t["gene"], exon_order=e["exon_order"],
                             n_exons=len(ex), is_terminal=int(e["is_terminal"]),
                             is_first=int(e["is_first"]), length=e["length"],
                             y=int(hits.get((name, e["exon_order"]), 0) > 0)))
    ex_df = pd.DataFrame(rows)
    ex_df = ex_df[ex_df.length > 0].copy()
    ex_df["log_len"] = np.log(ex_df.length)
    ex_df["rel_pos"] = (ex_df.exon_order - 1) / (ex_df.n_exons - 1)
    # keep only informative strata (at least one hit and at least one non-hit)
    g = ex_df.groupby("tx").y.agg(["sum", "count"])
    keep = g[(g["sum"] > 0) & (g["sum"] < g["count"])].index
    ex_df = ex_df[ex_df.tx.isin(keep)].copy()
    print(f"\n--- PRIMARY within-transcript model ---")
    print(f"  informative transcripts (strata): {ex_df.tx.nunique()}")
    print(f"  exons: {len(ex_df)}   exons with a cut: {int(ex_df.y.sum())}")
    print(f"  terminal-exon length vs internal (median nt): "
          f"{ex_df[ex_df.is_terminal==1].length.median():.0f} vs "
          f"{ex_df[ex_df.is_terminal==0].length.median():.0f}")

    from statsmodels.discrete.conditional_models import ConditionalLogit
    for label, cols in (("terminal only", ["is_terminal"]),
                        ("terminal + log(length)", ["is_terminal", "log_len"]),
                        ("terminal + log(length) + first",
                         ["is_terminal", "log_len", "is_first"])):
        try:
            m = ConditionalLogit(ex_df.y.values, ex_df[cols].values,
                                 groups=ex_df.tx.values).fit(disp=False)
            print(f"\n  [{label}]")
            for nm, b, se in zip(cols, m.params, m.bse):
                lo, hi = b - 1.96 * se, b + 1.96 * se
                z = b / se
                p = 2 * (1 - 0.5 * (1 + math.erf(abs(z) / math.sqrt(2))))
                print(f"    {nm:14s} beta {b:+.4f}  SE {se:.4f}  OR {math.exp(b):7.3f} "
                      f"[{math.exp(lo):.3f}, {math.exp(hi):.3f}]  z {z:+.2f}  p {p:.3g}")
        except Exception as exc:
            print(f"  [{label}] model failed: {exc}")

    # ---- SECONDARY: between-transcript -------------------------------------
    import statsmodels.api as sm
    cut_tx = set(t["name"] for c, t in assigned)
    brows = []
    seen = set()
    for t in tx:
        if t["name"] in seen or len(t["starts"]) < 2 or t["cdsStart"] == t["cdsEnd"]:
            continue
        seen.add(t["name"])
        u3, te, el = utr3_length(t), terminal_exon_length(t), exonic_length(t)
        if not (u3 and u3 > 0 and te > 0 and el > 0):
            continue
        brows.append(dict(tx=t["name"], y=int(t["name"] in cut_tx),
                          log_term=np.log(te), log_utr3=np.log(u3),
                          log_txlen=np.log(el), n_exons=len(t["starts"])))
    b = pd.DataFrame(brows)
    print(f"\n--- SECONDARY between-transcript model ---")
    print(f"  transcripts: {len(b)}   with >=1 cut: {int(b.y.sum())} "
          f"({100*b.y.mean():.2f}%)")
    print("  NOTE: baseline expression is NOT controlled here. Cut-site detection "
          "requires expression,\n        so any positive coefficient may partly "
          "reflect abundance rather than architecture.")
    for label, cols in (("3'UTR length only", ["log_utr3"]),
                        ("terminal-exon length only", ["log_term"]),
                        ("terminal + 3'UTR", ["log_term", "log_utr3"]),
                        ("full", ["log_term", "log_utr3", "log_txlen", "n_exons"])):
        X = sm.add_constant(b[cols])
        r = sm.Logit(b.y.values, X).fit(disp=False)
        print(f"\n  [{label}]  pseudo-R2 {r.prsquared:.4f}  LLF {r.llf:.1f}")
        for nm, bb, se, pv in zip(X.columns, r.params, r.bse, r.pvalues):
            if nm == "const":
                continue
            print(f"    {nm:12s} beta {bb:+.4f}  SE {se:.4f}  OR {math.exp(bb):6.3f} "
                  f"[{math.exp(bb-1.96*se):.3f}, {math.exp(bb+1.96*se):.3f}]  p {pv:.3g}")

    cut.to_csv("cut_level.tsv", sep="\t", index=False)
    ex_df.to_csv("exon_level.tsv", sep="\t", index=False)
    b.to_csv("tx_level.tsv", sep="\t", index=False)
    print("\nwrote cut_level.tsv, exon_level.tsv, tx_level.tsv")


if __name__ == "__main__":
    main()
