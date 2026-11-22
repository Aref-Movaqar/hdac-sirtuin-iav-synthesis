# Gate 1 result: sequence variation at the NP and PA modification sites

Run 21 November 2026. Sequences from NCBI, seven strains, NP (498 aa) and PA
(716 aa) with no indels in either protein, so column-wise comparison is valid.
NP identity to PR8 ranges 81.9 to 100 percent, PA identity 95.7 to 100 percent.

Accessions used. NP: NP_040982 (PR8), ACF54602.1 (WSN), ABF21286.1 (New
Caledonia/20/1999), ACP44151.1 (California/04/2009), ACJ47910.1
(env/Qinghai/1/2008 H5N1), ANK77952.1 (seal/Mass/1-SC35M/1980 H7N7),
AKU46787.1 (Anhui/1/2013 H7N9). PA: NP_040986.1, ACF54605.1, ACF41885.1,
ACP44156.1, ACJ47913.1, ABB90272.1, AKU46790.1 respectively.

Two notes on strain sourcing. A/Anhui/1/2013 is represented by the
reverse-genetics clone A/Anhui/1-YK_RG202/2013, since the parental isolate is
not retrievable under that designation in NCBI. SC35M is represented by
A/seal/Mass/1-SC35M_RG18/1980; the parental A/Seal/Massachusetts/1/1980 entry
(UniProt P26053) is SC35, not the mouse-adapted derivative.

---

## 1. NP acetylation sites, P1 residue with five flanking residues each side

### K103 — the flanks are variable, and two substitutions change charge

| strain | motif (−5 to +5) | identical to PR8 | substitutions |
|---|---|---|---|
| PR8 (H1N1, 1934) | `RRVNG[K]WMREL` | reference | — |
| WSN (H1N1, 1933) | `RRVDG[K]WRREL` | no | N101D (0→−), M105R (0→+) |
| New Caledonia/20/99 (H1N1) | `KRVDG[K]WVREL` | no | R98K, N101D (0→−), M105V |
| California/04/09 (pH1N1) | `RRVDG[K]WMREL` | no | N101D (0→−) |
| env/Qinghai/1/08 (H5N1) | `RRRDG[K]WMREL` | no | V100R (0→+), N101D (0→−) |
| SC35M (H7N7, mouse-ad.) | `RRRDG[K]WMREL` | no | V100R (0→+), N101D (0→−) |
| Anhui/1/2013 (H7N9) | `RRRDG[K]WVREL` | no | V100R (0→+), N101D (0→−), M105V |

K103 itself is invariant. The local context is not. Position 100 carries
valine in all three human H1N1 strains and arginine in all three
avian-origin strains, which is a clean human/avian split introducing a
positive charge three residues N-terminal to the target lysine. Position 101
is asparagine in PR8 alone and aspartate in all six others.

### K113 — effectively invariant

| strain | motif | substitutions |
|---|---|---|
| PR8, WSN, California/04/09, Qinghai H5N1, SC35M, Anhui H7N9 | `LILYD[K]EEIRR` | none |
| New Caledonia/20/99 | `LVLYD[K]EEIRR` | I109V |

### K229 — completely invariant across all seven strains

Every strain carries `NILKG[K]FQTAA`. No substitution anywhere in the eleven-residue
window, across H1N1, H5N1, H7N7 and H7N9.

---

## 2. PA K664 — completely invariant across all seven strains

Every strain carries `SAESR[K]LLLIV`. No substitution anywhere in the window,
including the three avian-origin strains.

---

## 3. PA-X C-terminal length

Computed from each PA coding sequence by applying the +1 frameshift after PA
codon 191 and translating to the first in-frame stop. Two independent controls
passed: SC35M returns a 252-residue PA-X, matching UniProt P0DJU3, and
California/04/2009 returns the 232-residue form known for pandemic 2009 H1N1.

| strain | X-ORF (aa) | PA-X total (aa) |
|---|---|---|
| PR8 (H1N1, 1934) | 61 | 252 |
| WSN (H1N1, 1933) | 61 | 252 |
| New Caledonia/20/99 (H1N1) | 61 | 252 |
| **California/04/09 (pH1N1)** | **41** | **232** |
| env/Qinghai/1/08 (H5N1) | 61 | 252 |
| SC35M (H7N7, mouse-ad.) | 61 | 252 |
| Anhui/1/2013 (H7N9) | 61 | 252 |

---

## 4. Verdict on Module 2a: NO-GO

Not because the flanks are identical. They are not. The hypothesis fails for two
other reasons, either of which is sufficient.

**The primary literature has already excluded the mechanism.** The pro-viral
HDAC1 result is Chen L, Wang C, Luo J, et al., *Front Immunol* 2017;8:1757, and
the paper is titled "Histone Deacetylase 1 Plays an **Acetylation-Independent**
Role in Influenza A Virus Replication." Its conclusion is that HDAC1 supports
replication independently of K103 deacetylation: in HDAC1-depleted cells the
K103 mutants and wild-type virus behaved the same. If HDAC1's effect does not
run through K103 acetylation, variation in the K103 flanks has no mechanism to
act through, and a selection analysis would be testing a hypothesis the source
paper has already ruled out.

**The study design removes subtype as the discriminating variable.** Chen et al.
obtained the pro-viral result across three viruses: A/environment/Qinghai/1/2008
(H5N1), **A/Beijing/05/2009 (H1N1)** and A/Chicken/Hangzhou/174/2013 (H7N9),
with the recombinant mutants built on the H5N1 backbone. A human H1N1 therefore
sits inside the pro-viral dataset. Whatever strain the opposing study used, a
strain or subtype explanation cannot account for the divergence, because the
pro-viral phenotype was reproduced in both an avian and a human-lineage virus
within one laboratory.

What this means for the manuscript: Section 4.1 should stop offering viral strain
as a plausible explanation for HDAC1's divergence. The remaining candidates are
laboratory, cell system, readout and timepoint, and that is a cleaner and more
defensible resolution than the current wording. It also aligns with the
correction already planned for the Abstract, from NP deacetylation to
NP-associated and acetylation-independent. That correction is not cosmetic; it
removes the premise of the module.

I could not confirm the exact strain used by Nagesh & Husain 2016 (ASM blocks
retrieval, PMC is behind a CAPTCHA, and the abstract does not name it). The
Husain laboratory's documented strain elsewhere is A/PR/8/1934. This does not
affect the verdict, which rests on the composition of Chen's panel rather than
on the comparator.

---

## 5. What the gate produced that is worth keeping

**PA K664 is universally conserved.** The HDAC6 deacetylation target site and its
entire eleven-residue context are identical across H1N1, H5N1, H7N7 and H7N9.
That supports generalisability of the HDAC6–PA mechanism across subtypes, which
is a claim Sections 4.2 and 8.2 currently do not make and could.

**K229's invariance reframes the convergence argument.** Section 4.1 presents the
agreement of two unconnected laboratories on K229, using different strains, as
strong independent corroboration. The eleven-residue context is identical across
all seven strains, so convergence on that residue is what one would expect and is
less surprising than presented. The residue's importance is unaffected; the
rhetorical weight placed on cross-strain agreement should come down.

**The PA-X length caveat is now quantified.** Section 5.4 warns that lineages vary
in PA-X length so that results from laboratory-adapted strains may not generalise.
Six of these seven strains carry the full-length 61-residue X-ORF; only pandemic
2009 H1N1 is truncated. The caveat is real but narrow, and it does not apply to
PR8-based work, including the GSE120183 dataset used in Gate 2.

**An inconsistency resolves itself.** Nagesh & Husain's abstract reports HDAC1
knockdown increasing viral growth "by >3-fold by 24 h and by >6-fold by 48 h."
The Table 1 entry of "3–6-fold" and the Figure 1 entry of ">6-fold" are both
partially right and were flagged as contradictory. The accurate phrasing is
greater than 3-fold at 24 hours and greater than 6-fold at 48 hours.

---

## 6. Recommended next step

Drop the HyPhy campaign and the AlphaFold complex predictions with it. Keep a
single supplementary alignment panel showing K229 and PA K664 invariance beside
K103 flank variability, which costs nothing and supports two generalisability
claims. Redirect the saved effort to Gate 3, the cut-site analysis on GSE207253,
which is now the gate that decides whether the paper has a mechanism.
