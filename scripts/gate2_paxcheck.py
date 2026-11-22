#!/usr/bin/env python3
"""
Gate 2. Are HDAC and sirtuin transcripts PA-X-dependently depleted during
infection, in an independent laboratory's transcriptome-wide dataset?

Data: GEO GSE120183, "Profiling of RNAs downregulated by influenza A virus
PA-X ribonuclease" (Gaucherand et al., Cell Rep 2019). A549 cells infected
with A/Puerto Rico/8/1934 wild type or one of three PA-X-null mutants
(PA(fs), PA(X9), PA(deltaX)), quantified against mock. Values are
log2 attomole ratios, so the platform is absolute-quantification rather than
RNA-seq and covers ~9,500 transcripts, not the whole transcriptome.

PA-X-specific effect = (WT vs mock) - (PA-X-null vs mock). A negative value
means the transcript is lost in the presence of PA-X and retained without it.

This is a scouting analysis on summary-level data. Percentiles are positions
in the transcript distribution, not p-values. Replicate standard deviations
are in the file and a proper per-gene test should use them, with multiplicity
control, before anything here is reported as a result.

Usage: python3 -I gate2_paxcheck.py IAV_results.txt
"""
import bisect, statistics as st, sys

GENES = {
    "HDAC1": "NM_004964", "HDAC2": "NM_001527", "HDAC3": "NM_003883",
    "HDAC4": "NM_006037", "HDAC5": "NM_005474", "HDAC6": "NM_006044",
    "HDAC7": "NM_015401", "HDAC8": "NM_018486", "HDAC9": "NM_014707",
    "HDAC10": "NM_032019", "HDAC11": "NM_024827",
    "SIRT1": "NM_012238", "SIRT2": "NM_012237", "SIRT3": "NM_012239",
    "SIRT4": "NM_012240", "SIRT5": "NM_012241", "SIRT6": "NM_016539",
    "SIRT7": "NM_016538",
}
I_WT, I_FS, I_X9, I_DX = 0, 2, 4, 6
SD_WT, SD_FS, SD_DX = 1, 3, 7


def load(path):
    rows = {}
    with open(path) as f:
        f.readline()
        for line in f:
            p = line.rstrip("\n").split("\t")
            rows[p[0]] = [float(x) if x not in ("", "NA", "NaN") else None
                          for x in p[1:]]
    return rows


def main():
    rows = load(sys.argv[1] if len(sys.argv) > 1 else "IAV_results.txt")

    def eff(v, i):
        return None if (v[I_WT] is None or v[i] is None) else v[I_WT] - v[i]

    bg = {i: sorted(x for v in rows.values() if (x := eff(v, i)) is not None)
          for i in (I_FS, I_X9, I_DX)}

    def pct(x, i):
        a = bg[i]
        return 100 * bisect.bisect_left(a, x) / len(a)

    print(f"{len(rows)} transcripts quantified\n")
    print(f"{'gene':8s}{'WT':>7s}{'fs':>7s}{'X9':>7s}{'dX':>7s}"
          f"{'PAX(fs)':>9s}{'pct':>6s}{'PAX(dX)':>9s}{'pct':>6s}  note")
    vals = []
    for g, a in GENES.items():
        v = rows.get(a)
        if v is None:
            print(f"{g:8s}{'not quantified on this platform':>48s}")
            continue
        e_fs, e_dx = eff(v, I_FS), eff(v, I_DX)
        fmt = lambda x, w=7: f"{x:+{w}.2f}" if x is not None else " " * (w - 2) + "na"
        p_fs = f"{pct(e_fs, I_FS):6.1f}" if e_fs is not None else "    na"
        p_dx = f"{pct(e_dx, I_DX):6.1f}" if e_dx is not None else "    na"
        note = ""
        if e_dx is not None and e_dx > 0:
            note = "retained WITH PA-X (opposite direction)"
        elif e_dx is not None and pct(e_dx, I_DX) < 15:
            note = "strongly PA-X-dependent"
        print(f"{g:8s}{fmt(v[I_WT])}{fmt(v[I_FS])}{fmt(v[I_X9])}{fmt(v[I_DX])}"
              f"{fmt(e_fs,9)}{p_fs}{fmt(e_dx,9)}{p_dx}  {note}")
        if e_fs is not None:
            vals.append((g, e_fs, e_dx))

    print()
    for i, name in ((I_FS, "PA(fs)"), (I_DX, "PA(deltaX)")):
        print(f"background median, {name}: {st.median(bg[i]):+.3f}  (n={len(bg[i])})")
    fam = [v[1] for v in vals]
    print(f"\nHDAC/sirtuin set median, PA(fs) contrast: {st.median(fam):+.3f}")
    print("Set-vs-background enrichment should be tested with a rank test on the "
          "quantified subset, not read off these medians.")


if __name__ == "__main__":
    main()
