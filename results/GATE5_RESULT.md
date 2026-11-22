# Gate 5 result: independent proteomics does not replicate HDAC/sirtuin protein depletion, except for HDAC2

Run 21 November 2026. Three published quantitative IAV proteomics datasets, all
from laboratories independent of the Husain group.

| # | dataset | what it measures | system | depth |
|---|---|---|---|---|
| 1 | Krogan lab, *Nat Commun* 2023 | whole-cell **abundance**, log2FC vs mock | NHBE and PMA-THP-1; pH1N1 California/04/2009, H3N2 Wyoming/03/2003, H5N1 Vietnam/1203/2004; 3, 6, 12, 18 h | 3,697 proteins, 22 conditions |
| 2 | Bogdanow et al., *Nat Commun* 2019, PXD011321 | **newly synthesised** protein (pAHA-SILAC) | A549; H3N2 Panama/2007/1999 and avian H3N2 Mallard/439/2004; AHA pulses 0-4, 4-8, 8-12, 12-16 h | 7,729 rows |
| 3 | Huang, Urban, Hubel, Stukalov & Pichlmair, *Cell Syst* 2024;15(10):911-929.e8, PXD047063 | **synthesis and degradation rates separately**, plus abundance | HeLa, MOI 3, n=4; IAV and IAVΔNS1; 12, 18, 24, 30, 36, 42 h | 7,579 protein groups |

Dataset 3 was not in the original plan and is the one that settles the question.
Its pulse-chase design estimates, per protein, the degradation rate of material
made **before** infection (d0), the degradation rate of material made after
(d1), the synthesis rate (s), and a synthesis rate corrected for global
translational shutoff (s_corrected). A claim that influenza destroys an enzyme
predicts a rise in d0. Nothing else in the public record tests that directly.

## Verdict: NO-GO for Module 3b as planned, GO for a narrower and better claim

Module 3b was meant to replicate, in independent data, the Western-blot
depletion of HDAC1, HDAC2, HDAC4, HDAC6, HDAC8, HDAC11 and SIRT1-3. That cannot
be done. Two of those enzymes are never quantified in any of the three datasets,
and for most of the rest the independent data return a precise null or the
opposite sign.

What survives is narrower, cleanly supported, and in one respect more
interesting than the original aim: **HDAC2 is specifically destabilised**, and
**HDAC1 behaves in a strain-dependent way that reverses sign**.

---

## 1. Coverage: five of the eighteen enzymes are invisible to mass spectrometry

✓ = quantified, · = protein not detected.

| enzyme | Krogan (abundance) | Bogdanow (synthesis) | Pichlmair (turnover) | n datasets |
|---|---|---|---|---|
| HDAC1 | ✓ | ✓ | ✓ | 3 |
| HDAC2 | ✓ | ✓ | ✓ | 3 |
| HDAC3 | · | ✓ (no ratio) | ✓ | 2 |
| HDAC4 | · | ✓ | ✓ | 2 |
| HDAC5 | · | · | · | **0** |
| HDAC6 | · | ✓ | ✓ | 2 |
| HDAC7 | · | ✓ | ✓ | 2 |
| HDAC8 | · | · | ✓ | 1 |
| HDAC9 | · | · | · | **0** |
| HDAC10 | · | · | · | **0** |
| HDAC11 | · | · | · | **0** |
| SIRT1 | · | ✓ | ✓ | 2 |
| SIRT2 | ✓ | ✓ | ✓ | 3 |
| SIRT3 | · | ✓ | ✓ | 2 |
| SIRT4 | · | · | · | **0** |
| SIRT5 | · | ✓ | ✓ | 2 |
| SIRT6 | · | ✓ | ✓ | 2 |
| SIRT7 | · | ✓ | · | 1 |
| | **3/18** | **12/18** | **12/18** | |

Detected in at least one dataset: 13 of 18. Detected in all three: 3 (HDAC1,
HDAC2, SIRT2). Never detected: **HDAC5, HDAC9, HDAC10, HDAC11, SIRT4**.

Two points follow, and they are different in kind.

**"Not detected" here means not detected, not unchanged.** HDAC11 is absent from
all three datasets. No reanalysis of public proteomics can speak to HDAC11
protein levels in infection, in either direction. The same holds for HDAC5,
HDAC9, HDAC10 and SIRT4. Any manuscript sentence implying proteome-level support
for those enzymes has to go.

**Detection is not the limiting factor for the rest.** Reference proteins behave
as published in every dataset: CTTN, STAT1, GPKOW, KPNA6, POLR2A and PPP6C are
all quantified and all recover their reported phenotypes. The nulls below are
therefore nulls, not sensitivity failures.

A caveat specific to dataset 3: the 12-enzyme coverage is for the **turnover
model**, which pools all SILAC channels and timepoints. Direct abundance ratios
with at least two replicates in both arms are estimable for only **HDAC1, HDAC2
and HDAC7** across the full time course, plus HDAC3, SIRT1 and SIRT6 at 12 h
alone. The model is more sensitive than the raw ratio, which is why the two
coverage figures differ.

---

## 2. Direction and magnitude

### 2a. Degradation rate, the direct test (Pichlmair, IAV vs mock)

Δd0 is the change in degradation rate of enzyme made before infection. The
authors' own hit threshold is |Δd| ≥ 0.25 with p ≤ 0.001.

| enzyme | Δd0 | SD | \|Δ\|/SD | p | percentile | hit |
|---|---|---|---|---|---|---|
| **HDAC2** | **+0.3029** | 0.0571 | 5.30 | **8.9e-33** | **94.7** | **YES** |
| HDAC1 | −0.0628 | 0.2124 | 0.30 | 0.74 | 18.2 | no |
| SIRT6 | +0.0001 | 0.1096 | 0.00 | 0.99 | 54.0 | no |
| HDAC3 | +0.0004 | 0.0523 | 0.01 | 0.93 | 70.2 | no |
| HDAC4 | −0.0009 | 0.0347 | 0.03 | 0.87 | 26.9 | no |
| HDAC6 | −0.0005 | 0.0304 | 0.02 | 0.89 | 30.6 | no |
| HDAC7 | +0.0001 | 0.0070 | 0.01 | 0.97 | 54.2 | no |
| HDAC8 | +0.0003 | 0.0397 | 0.01 | 0.94 | 68.0 | no |
| SIRT1 | +0.0004 | 0.0476 | 0.01 | 0.89 | 70.8 | no |
| SIRT2 | −0.0001 | 0.0490 | 0.00 | 0.90 | 42.2 | no |
| SIRT3 | +0.0001 | 0.0351 | 0.00 | 0.98 | 60.7 | no |
| SIRT5 | +0.0007 | 0.0290 | 0.02 | 0.84 | 74.7 | no |
| *POLR2A* | *−2.8893* | *0.4* | | *2.3e-04* | *0.4* | *YES* |
| *GPKOW* | *−1.6212* | | | *4.8e-220* | *1.5* | *YES* |
| *KPNA6* | *−0.8073* | | | *2.2e-84* | *4.2* | *YES* |
| *PPP6C* | *−0.8556* | | | *5.3e-45* | *3.9* | *YES* |

The posterior SDs matter here, and they are what turn this from "no signal" into
a result. For HDAC3, HDAC4, HDAC6, HDAC7, HDAC8, SIRT1, SIRT2, SIRT3 and SIRT5
the SD is 0.007 to 0.052, so the 95% interval is roughly ±0.06 to ±0.10. That
**excludes the 0.25 hit threshold by a wide margin**. These are precise nulls:
infection does not accelerate the degradation of these enzymes, and the data are
good enough to say so rather than merely to fail to reject.

Two enzymes are genuinely inconclusive on degradation, and should be reported as
such rather than as nulls: **HDAC1** (SD 0.212, interval about ±0.42, which
contains 0.25) and **SIRT6** (SD 0.110, interval about ±0.21, at the margin).

**HDAC2 is the exception and it is a strong one.** Δd0 = +0.303, 5.3 posterior
SDs from zero, 94.7th percentile of the proteome, and the same direction and
magnitude for protein made after infection (Δd1 = +0.349, p = 3.9e-16, 94.2nd
percentile). It also holds for IAVΔNS1 (Δd0 = +0.202, p = 4.5e-8, 93.5th
percentile), and the direct IAV versus IAVΔNS1 contrast is not significant
(+0.107, p = 0.058). So HDAC2 destabilisation is real, specific, and **does not
require NS1**.

### 2b. Synthesis, corrected for host shutoff (Pichlmair, IAV vs mock)

No HDAC or sirtuin is a hit on s_corrected. The nominally significant values run
*positive*: HDAC6 +1.010 (p = 0.083), HDAC8 +0.501, SIRT5 +0.498, SIRT6 +0.480
(p = 0.031), HDAC1 +0.433 (p = 0.030), HDAC4 +0.426. HDAC3 (−2.019, p = 0.043)
and SIRT1 (−18.16, p = 0.0012) run negative, but SIRT1's magnitude of 18 on a
scale where most proteins sit below 2 indicates a poorly constrained parameter
for a low-abundance protein, and I would not report it.

### 2c. Synthesis (Bogdanow): the apparent depletion is host shutoff, and these enzymes are *spared*

This is the correction that changes the reading of this dataset. Raw
infected-to-mock synthesis ratios late in infection look dramatic: HDAC1 −2.33
at 8-12 h, HDAC6 −1.88 at 12-16 h, SIRT1 −3.23 at 8-12 h. But the **median host
protein** at those intervals is −2.56 and −2.48. Expressed as a percentile of
the whole-proteome distribution for the same interval:

| enzyme | interval | ratio | proteome median | percentile |
|---|---|---|---|---|
| HDAC4 | 12-16 h | −1.58 | −2.48 | **94.6** |
| HDAC6 | 12-16 h | −1.88 | −2.48 | **88.7** |
| SIRT6 | 8-12 h | −1.92 | −2.56 | 86.7 |
| HDAC1 | 8-12 h | −2.33 | −2.56 | 66.1 |
| HDAC2 | 8-12 h | −2.37 | −2.56 | 62.9 |
| SIRT2 | 8-12 h | −2.55 | −2.56 | 51.3 |
| HDAC7 | 8-12 h | −3.13 | −2.56 | 14.5 |
| SIRT1 | 8-12 h | −3.23 | −2.56 | 11.2 |

HDAC4 and HDAC6 synthesis is better preserved than roughly 90% of the host
proteome. The human-versus-avian (Pan.Mal) ratios are near zero throughout,
which is what global shutoff predicts and targeted antagonism does not. Only
HDAC7 and SIRT1 fall below the median, and neither is a manuscript claim.

**Any uncontextualised late-infection fold change from this dataset would have
been read backwards.** That is worth stating in the manuscript's methods as a
general caution, because the same trap applies to every shutoff-era proteomics
comparison.

### 2d. Abundance (Krogan): HDAC1 reverses sign by strain

HDAC1 was quantified in 20 of 22 conditions, range −2.089 to +1.055, and the
direction is not inconsistent noise. It is organised by strain:

| condition group | values | percentiles |
|---|---|---|
| H3N2 (NHBE and THP-1) | −1.500, −1.240, −1.866, −0.919, −0.569, −2.089 | 3.1, 19.2, **1.8**, 5.6, 16.8, **3.7** |
| pH1N1, THP-1 | −1.074, −1.218, −0.578 | **2.8**, **4.6**, 33.2 |
| pH1N1, NHBE | −0.262, +0.102, +0.532 | 37.5, 44.8, 87.0 |
| **H5N1, THP-1** | **+1.055, +0.629, +0.213, +0.481** | **96.8, 94.7, 85.1, 90.6** |
| H5N1, NHBE | −0.370, −0.623, +0.432, +0.072 | 32.7, 37.4, 88.1, 55.7 |

H3N2 depletes HDAC1 into the bottom few percent of the proteome. H5N1 in THP-1
raises it into the top 5 to 10%. Only one condition reaches significance after
multiple-testing correction (H3N2_THP1_18H, adj. p = 0.025), so this is an
observation and not a tested effect, but the pattern is coherent across eight
independent conditions and it is the kind of thing the Three-Axis framework
exists to accommodate.

HDAC2 in the same dataset rises early (five of six 3 h conditions positive, up
to +1.785 at the 98.8th percentile) and falls late. SIRT2 is quantified in only
3 of 22 conditions, two of them −Inf, and is uninformative.

**A handling note on −Inf.** The Krogan table contains 9,739 −Inf entries, up to
1,071 within a single condition. −Inf means the protein was not detected in the
infected sample, which at 18 h coincides with a collapse in global detection. It
is a detection boundary, not a measured fold change, and it must be excluded
from distributions and never read as infinite depletion. HDAC2 has four and
SIRT2 two.

---

## 3. What this means for the manuscript

**Remove**, because independent data contradict or cannot address them:

- Any proteome-level support for HDAC5, HDAC9, HDAC10, HDAC11 or SIRT4. Not
  detected anywhere.
- Any claim that infection accelerates degradation of HDAC4, HDAC6, HDAC8,
  SIRT1, SIRT2, SIRT3 or SIRT5. Precise nulls, intervals excluding the effect
  size by three- to eightfold.
- HDAC6 in particular. The manuscript's protein-level HDAC6 claim is the one
  most clearly refuted: degradation unchanged to within ±0.06, and synthesis
  better preserved than 89% of the proteome.

**Keep and promote**, because they are independently supported:

- **HDAC2 is destabilised during IAV infection**, in HeLa, by a pulse-chase
  method in an independent laboratory, at 5.3 posterior SDs, in the top 5% of
  the proteome, for pre-existing and newly made protein alike, and without
  requiring NS1. This is a genuine replication of a protein-level antagonism
  claim, and it is the only one.
- **HDAC1 protein response is strain-dependent and changes sign**, depleted by
  H3N2 and pH1N1 and elevated by H5N1 in macrophage-like cells. Read together
  with Gate 1, where NP K229 and PA K664 were completely invariant across the
  same strain panel, this says the divergence in the HDAC1 literature is not
  explained by sequence variation at the relevant residues. The axis is strain
  and cell type, not target sequence.

**State as an open limitation:** HDAC1 and SIRT6 degradation rates are
inconclusive in the only dataset that measures them, and no public dataset
quantifies HDAC11 protein at all.

---

## 4. Limitations

**Three datasets, three quantities.** Abundance, synthesis and turnover are not
interchangeable, and only Krogan and the Pichlmair abundance arm measure what a
whole-cell Western blot measures. The strongest result (HDAC2) comes from
turnover, which no Western blot in the manuscript's source literature measured.

**Cell systems do not match.** HeLa (Pichlmair), A549 (Bogdanow), NHBE and
PMA-THP-1 (Krogan). None is the system in which the original HDAC4, HDAC6 or
HDAC11 Westerns were run, and HeLa is not a respiratory cell. A null in HeLa
does not strictly exclude an effect in A549.

**Strains differ, and the strain matters.** Section 2d shows HDAC1 reversing by
strain, which means a null in one strain is weak evidence about another. The
PXD047063 deposit does not name its IAV/IAVΔNS1 pair; that needs taking from the
paper's methods, which are paywalled, before anything is written.

**Pichlmair p-values are uncorrected** by the authors' own statement, and come
from a Bayesian turnover model rather than a frequentist test. HDAC2 survives
any reasonable correction at p = 9e-33; the marginal values (HDAC1 s_corrected
p = 0.030, SIRT6 p = 0.031) do not and should not be reported as significant.

**Percentile framing is descriptive.** It locates an enzyme in the proteome-wide
distribution for the same condition, which is what distinguishes specific from
global, but it is not a formal test against a matched background. If the HDAC2
and HDAC1 results are reported, a matched null (abundance-matched and
compartment-matched proteins, cluster bootstrap) should replace the percentile.

**Only three datasets.** A fourth independent abundance dataset in A549 or
primary airway cells would strengthen the HDAC6 null considerably, since that
null currently rests on HeLa turnover and A549 synthesis but on no A549
abundance measurement.
