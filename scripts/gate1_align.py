#!/usr/bin/env python3
"""
Gate 1. Does sequence variation around the NP acetylation sites, or around
PA K664, track the strains in which HDAC1 and HDAC6 phenotypes diverge?

Reports, across seven strains:
  1. NP K103, K113, K229 with +/-5 flanking residues, and any charge change
  2. PA K664 with +/-5 flanking residues
  3. PA-X C-terminal (X-ORF) length, computed from the PA coding sequence by
     applying the +1 ribosomal frameshift after codon 191 and translating to
     the first in-frame stop

PA-X control: A/seal/Mass/1-SC35M/1980 should give a 252-residue PA-X
(191 + 61), matching UniProt P0DJU3.

Usage: python3 -I gate1_align.py
"""
import re, sys, time, urllib.parse, urllib.request

NP = {  # label -> protein accession
    "PR8 (H1N1, 1934)":            "NP_040982",
    "WSN (H1N1, 1933)":            "ACF54602.1",
    "New Caledonia/20/99 (H1N1)":  "ABF21286.1",
    "California/04/09 (pH1N1)":    "ACP44151.1",
    "env/Qinghai/1/08 (H5N1)":     "ACJ47910.1",
    "SC35M (H7N7, mouse-ad.)":     "ANK77952.1",
    "Anhui/1/2013 (H7N9)":         "AKU46787.1",
}
PA = {
    "PR8 (H1N1, 1934)":            ("NP_040986.1", "NC_002022.1", 25, 2175),
    "WSN (H1N1, 1933)":            ("ACF54605.1",  "CY034137.1",  11, 2161),
    "New Caledonia/20/99 (H1N1)":  ("ACF41885.1",  "CY033627.1",   9, 2159),
    "California/04/09 (pH1N1)":    ("ACP44156.1",  "FJ969515.1",   1, 2151),
    "env/Qinghai/1/08 (H5N1)":     ("ACJ47913.1",  "FJ455825.1",   1, 2151),
    "SC35M (H7N7, mouse-ad.)":     ("ABB90272.1",  "DQ266099.1",  25, 2175),
    "Anhui/1/2013 (H7N9)":         ("AKU46790.1",  "CY193256.1",  13, 2163),
}
NP_SITES = (103, 113, 229)
PA_SITES = (664,)
FS_CODON = 191          # +1 frameshift occurs after this PA codon
POS, NEG = set("KRH"), set("DE")
CODON = {}
for i, b1 in enumerate("TCAG"):
    for b2 in "TCAG":
        for b3 in "TCAG":
            CODON[b1 + b2 + b3] = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"[
                len(CODON)]


def efetch(db, ids, rettype):
    url = ("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?"
           + urllib.parse.urlencode({"db": db, "id": ids, "rettype": rettype,
                                     "retmode": "text"}))
    for a in range(3):
        try:
            with urllib.request.urlopen(url, timeout=90) as r:
                return r.read().decode()
        except Exception:
            if a == 2:
                raise
            time.sleep(3 * (a + 1))


def fasta_map(txt):
    out, k = {}, None
    for line in txt.split("\n"):
        if line.startswith(">"):
            k = line[1:].split()[0].split("|")[0].split(".")[0]
            out[k] = []
        elif k:
            out[k].append(line.strip())
    return {k: "".join(v) for k, v in out.items()}


def charge(a):
    return "+" if a in POS else ("-" if a in NEG else "0")


def window(seq, pos, flank=5):
    lo, hi = max(0, pos - 1 - flank), min(len(seq), pos + flank)
    return seq[lo:pos - 1], seq[pos - 1], seq[pos:hi]


def show(name, seqs, sites, ref_label):
    ref = seqs[ref_label]
    for site in sites:
        print(f"\n--- {name} position {site} (+/-5), reference {ref_label} ---")
        rl, rc, rr = window(ref, site)
        print(f"  {'strain':30s} {'motif':14s} {'P1':>3s}  identical_to_ref  substitutions")
        for lab, s in seqs.items():
            if len(s) < site:
                print(f"  {lab:30s} sequence too short"); continue
            l, c, r = window(s, site)
            motif = f"{l}[{c}]{r}"
            same = (l == rl and c == rc and r == rr)
            subs = []
            for i, (a, b) in enumerate(zip(rl + rc + rr, l + c + r)):
                if a != b:
                    off = i - len(rl)
                    subs.append(f"{a}{site+off}{b}"
                                + ("" if charge(a) == charge(b)
                                   else f"({charge(a)}->{charge(b)})"))
            print(f"  {lab:30s} {motif:14s} {c:>3s}  {'yes' if same else 'NO ':16s} "
                  f"{', '.join(subs) if subs else '-'}")


def pax_xorf(cds):
    """Apply +1 frameshift after codon FS_CODON; return (xorf_aa, length)."""
    nt = cds[(FS_CODON * 3) + 1:]          # skip one nucleotide -> +1 frame
    aa = []
    for i in range(0, len(nt) - 2, 3):
        c = CODON.get(nt[i:i + 3].upper().replace("U", "T"), "X")
        if c == "*":
            break
        aa.append(c)
    return "".join(aa), len(aa)


def main():
    print("Gate 1: NP and PA sequence variation at the modification sites\n")

    prot = fasta_map(efetch("protein", ",".join(NP.values()), "fasta"))
    npseq = {lab: prot[acc.split(".")[0]] for lab, acc in NP.items()}
    lens = {len(s) for s in npseq.values()}
    print(f"NP lengths: {lens}  ({'no indels, column comparison valid' if len(lens)==1 else 'INDELS PRESENT, align first'})")
    ref = "PR8 (H1N1, 1934)"
    for lab, s in npseq.items():
        ident = 100 * sum(a == b for a, b in zip(s, npseq[ref])) / len(s)
        print(f"   {lab:30s} {len(s)}aa  identity to PR8 {ident:5.1f}%")
    show("NP", npseq, NP_SITES, ref)

    paprot = fasta_map(efetch("protein", ",".join(v[0] for v in PA.values()), "fasta"))
    paseq = {lab: paprot[v[0].split(".")[0]] for lab, v in PA.items()}
    lens = {len(s) for s in paseq.values()}
    print(f"\n\nPA lengths: {lens}  ({'no indels' if len(lens)==1 else 'INDELS PRESENT'})")
    for lab, s in paseq.items():
        ident = 100 * sum(a == b for a, b in zip(s, paseq[ref])) / len(s)
        print(f"   {lab:30s} {len(s)}aa  identity to PR8 {ident:5.1f}%")
    show("PA", paseq, PA_SITES, ref)

    print("\n\n--- PA-X C-terminal (X-ORF) length, +1 frameshift after PA codon 191 ---")
    print(f"  {'strain':30s} {'X-ORF':>6s} {'PA-X total':>11s}  X-ORF C-terminal sequence")
    for lab, (pacc, nacc, a, b) in PA.items():
        nt = fasta_map(efetch("nuccore", nacc, "fasta"))
        seg = list(nt.values())[0]
        cds = seg[a - 1:b]
        tr = "".join(CODON.get(cds[i:i + 3].upper(), "X") for i in range(0, len(cds) - 2, 3))
        ok = tr[:191] == paseq[lab][:191]
        xo, n = pax_xorf(cds)
        print(f"  {lab:30s} {n:>6d} {191+n:>11d}  {xo}"
              + ("" if ok else "   [WARNING: CDS translation disagrees with protein record]"))
        time.sleep(0.35)


if __name__ == "__main__":
    main()
