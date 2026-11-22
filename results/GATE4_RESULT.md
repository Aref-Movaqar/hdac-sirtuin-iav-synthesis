# Gate 4 result: the cancellation prediction is not testable with public screen data; the DepMap arm gives one clean result

Run 21 November 2026.

## Verdict: NO-GO for Module 1b as specified. GO for a narrower DepMap claim.

The Section 4.4 cancellation prediction cannot be tested to a useful standard,
for four reasons that compound. Only two published genome-wide IAV screens
release a continuous statistic for every gene. Those two do not correlate with
each other genome-wide. Neither of them detects even gene essentiality, so their
per-gene effect sizes are largely noise. And the one nominally positive
attenuation result is explained by measurement precision rather than biology, as
shown by a control that cannot be explained any other way.

The DepMap arm is different. It returns a clean, well-powered, directly useful
result that supports the manuscript's target/domain axis.

---

## 1. Dataset availability, which is the binding constraint

Ten genome-wide IAV screens are catalogued in the Pichlmair harmonisation, and
the Maes meta-analysis covers 15 proviral and 4 antiviral screens. Of all of
them, **two** publish a full gene-level table with a continuous statistic for
every gene:

| screen | design | genes | statistic |
|---|---|---|---|
| **Sharon 2020** *Sci Rep* 10:12166 | CRISPRn, HEK293SF, PR8-GFPΔHA, GFP sort, MAGeCK | **19,105** | signed gene-level LFC, **both directions tested** |
| **Yi 2022** *Cell Rep* 38:110559 | CRISPRn, A549, H7N9, cell viability, MAGeCK | **20,706** | LFC, `pos|` statistics only |

Everything else is truncated or unusable for a background comparison:

- **Li 2020** *Nat Commun* 11:164. The 'Secondary screen' sheet lists 18,291
  gene names but reports a p-value for only **874** of them. Of the 18 enzymes,
  only HDAC3 (combined p 0.244, FDR 0.084) and SIRT2 (p 0.644, FDR 0.230) carry
  any statistic at all.
- **Han 2018** *Cell Rep* 23:596. Publishes **1,679** positively selected genes
  (Rd2) and 510 (Rd5). None of the 18 appears in either list.
- **Song 2021** *PLoS Pathog* 17:e1010141. Enriched sgRNA lists only, under 300
  rows per round. HDAC10 appears once as a surviving sgRNA in round 2.
- **Brass, Karlas, König, Ward**: no retrievable full gene-level table. The
  Pichlmair harmonisation carries only binary hit calls for these, and is itself
  pre-filtered to turnover-affected proteins.
- **Heaton 2017** CRISPRa: the deposit is raw sgRNA read counts across a
  severely bottlenecked three-round selection (69,469 plasmid sgRNAs down to
  1,547 in round C). Deriving gene-level effects from that would be my analysis,
  not a published screen's, and not comparable to MAGeCK output.

**The Maes 2024 meta-analysis cannot be repurposed for this test.** Maes A,
Botzki A, Mathys J, Impens F, Saelens X, *J Virol* 2024;98(4):e0185723
(PMC11257101) uses MAIC, meta-analysis by information content, which aggregates
**ranked gene lists** into an evidence score. A MAIC score measures accumulated
evidence of being a hit. A gene with no evidence scores near zero, and so does a
gene whose opposing effects cancelled. The two are indistinguishable in MAIC
output by construction, which is precisely the discrimination Section 4.4
requires. The same objection applies to Li 2020's own MAIC table (20,446 genes,
per-category evidence scores).

So the requirement of three or more independent screens with full gene-level
scores **is not met by the public record**. That is the central finding of
Gate 4, and it is a statement about the field, not about this manuscript.

---

## 2. Coverage: complete, in sharp contrast to the proteomics

| | Sharon | Yi | Li |
|---|---|---|---|
| HDAC1-11, SIRT1-7 | **18/18** | **18/18** | 18/18 listed, 2/18 with statistics |

All 18 enzymes are present and scored in both full screens. Unlike Gate 5, where
HDAC5, HDAC9, HDAC10, HDAC11 and SIRT4 were never detected in any proteomics
dataset, CRISPR screens have no detection problem here. Absence of a result is
therefore a real absence of effect, not a measurement gap.

Both screens validate on their own positive controls. SLC35A1, the canonical IAV
sialic-acid entry factor, is rank 1 of 20,706 in Yi (centred LFC +16.26,
p = 2.4e-07) and neg-rank 6 of 19,105 in Sharon (centred LFC −0.867,
p = 2.6e-07). CYTH2, Yi's own headline hit, is rank 6 (p = 1.1e-04).

---

## 3. Exact gene-level statistics for the 18

### Sharon 2020 (library median LFC +0.0109)

| gene | sgRNA | LFC | centred | \|centred\| | pctile | pos p | pos FDR | pos rank | neg p | neg rank |
|---|---|---|---|---|---|---|---|---|---|---|
| HDAC1 | 4 | −0.0640 | −0.0749 | 0.0749 | 43.4 | 0.364 | 0.832 | 8299 | 0.0575 | 2148 |
| HDAC2 | 4 | +0.3277 | +0.3168 | 0.3168 | 96.0 | 0.0213 | 0.260 | 1562 | 0.934 | 16844 |
| HDAC3 | 4 | −0.3322 | −0.3431 | 0.3431 | 96.9 | 0.999 | 1 | 18987 | **0.00175** | **251** |
| HDAC4 | 4 | −0.0678 | −0.0787 | 0.0787 | 45.2 | 0.733 | 0.977 | 14304 | 0.186 | 4397 |
| HDAC5 | 4 | −0.0482 | −0.0591 | 0.0591 | 35.3 | 0.731 | 0.977 | 14236 | 0.237 | 5250 |
| HDAC6 | 4 | +0.1448 | +0.1339 | 0.1339 | 69.1 | 0.181 | 0.624 | 5513 | 0.848 | 15166 |
| HDAC7 | 4 | −0.0569 | −0.0679 | 0.0679 | 39.7 | 0.892 | 1 | 16953 | 0.189 | 4535 |
| HDAC8 | 4 | +0.1880 | +0.1771 | 0.1771 | 80.7 | **0.00878** | 0.186 | **886** | 0.995 | 18642 |
| HDAC9 | 4 | −0.1828 | −0.1937 | 0.1937 | 84.0 | 0.970 | 1 | 18297 | **0.00858** | **618** |
| HDAC10 | 4 | −0.0011 | −0.0120 | 0.0120 | 7.5 | 0.491 | 0.904 | 10276 | 0.210 | 4844 |
| HDAC11 | 4 | +0.0076 | −0.0033 | 0.0033 | 2.2 | 0.731 | 0.977 | 14259 | 0.827 | 14816 |
| SIRT1 | 4 | +0.0681 | +0.0572 | 0.0572 | 34.3 | 0.444 | 0.872 | 9658 | 0.902 | 16157 |
| SIRT2 | 3 | −0.0839 | −0.0948 | 0.0948 | 53.1 | 0.959 | 1 | 17911 | 0.536 | 10230 |
| SIRT3 | 4 | +0.1905 | +0.1796 | 0.1796 | 81.2 | 0.0765 | 0.421 | 3439 | 0.929 | 16758 |
| SIRT4 | 4 | +0.2740 | +0.2631 | 0.2631 | 92.7 | 0.0539 | 0.377 | 2637 | 0.961 | 17520 |
| SIRT5 | 3 | −0.0201 | −0.0310 | 0.0310 | 19.3 | 0.313 | 0.771 | 8236 | 0.816 | 14344 |
| SIRT6 | 4 | +0.1063 | +0.0954 | 0.0954 | 53.3 | 0.0626 | 0.389 | 3046 | 0.991 | 18494 |
| SIRT7 | 4 | +0.0969 | +0.0860 | 0.0860 | 48.9 | 0.368 | 0.835 | 8358 | 0.237 | 5248 |

### Yi 2022 (library median LFC −5.2896; the whole library dropped 5.3 log2 units, so raw LFC must be centred)

| gene | sgRNA | LFC | centred | \|centred\| | pctile | pos p | pos FDR | pos rank |
|---|---|---|---|---|---|---|---|---|
| HDAC1 | 6 | −5.4228 | −0.1332 | 0.1332 | 21.2 | 0.170 | 0.950 | 3536 |
| HDAC2 | 6 | −5.2733 | +0.0163 | 0.0163 | 2.7 | 0.516 | 0.981 | 10600 |
| HDAC3 | 5 | −5.0251 | +0.2645 | 0.2645 | 41.1 | 0.381 | 0.974 | 7906 |
| HDAC4 | 6 | −5.4088 | −0.1192 | 0.1192 | 19.0 | 0.944 | 1 | 19466 |
| HDAC5 | 6 | −5.3889 | −0.0993 | 0.0993 | 15.8 | 0.860 | 0.998 | 17811 |
| HDAC6 | 6 | −5.4683 | −0.1787 | 0.1787 | 28.4 | 0.081 | 0.931 | 1645 |
| HDAC7 | 6 | −5.7939 | −0.5043 | 0.5043 | 69.1 | 0.969 | 1 | 19967 |
| HDAC8 | 6 | −6.3181 | −1.0285 | 1.0285 | 94.2 | 0.754 | 0.993 | 15564 |
| HDAC9 | 6 | −5.1223 | +0.1673 | 0.1673 | 26.7 | 0.155 | 0.950 | 3272 |
| HDAC10 | 6 | −5.8296 | −0.5400 | 0.5400 | 72.4 | 0.544 | 0.982 | 11298 |
| HDAC11 | 6 | −6.1335 | −0.8439 | 0.8439 | 89.5 | 0.946 | 1 | 19512 |
| SIRT1 | 6 | −5.5178 | −0.2282 | 0.2282 | 36.0 | 0.816 | 0.997 | 16834 |
| SIRT2 | 6 | −5.4258 | −0.1362 | 0.1362 | 21.6 | 0.137 | 0.950 | 2800 |
| SIRT3 | 6 | −5.4750 | −0.1854 | 0.1854 | 29.6 | 0.952 | 1 | 19638 |
| SIRT4 | 6 | −5.4844 | −0.1948 | 0.1948 | 31.0 | 0.624 | 0.989 | 12945 |
| SIRT5 | 6 | −4.0785 | +1.2111 | 1.2111 | 96.5 | **0.0062** | 0.931 | **122** |
| SIRT6 | 6 | −5.4270 | −0.1374 | 0.1374 | 21.8 | 0.501 | 0.981 | 10384 |
| SIRT7 | 6 | −5.7253 | −0.4357 | 0.4357 | 62.3 | 0.860 | 0.998 | 17797 |

**No HDAC or sirtuin reaches FDR significance in either screen.** The best FDR
is 0.186 (HDAC8, Sharon) and 0.931 (SIRT5, Yi). The nominal signals do not
overlap between screens: Sharon flags HDAC3, HDAC8 and HDAC9; Yi flags SIRT5
only. Sign agreement across the two screens is **8/18**, where chance is 9/18.

---

## 4. The cancellation test

Effect size: |LFC centred on the library median|. The prediction is directional,
so "indistinguishable from background" **fails** it.

### Matched permutation test (matched on sgRNA count, 20,000 draws)

| screen | target median | matched null median | ratio | percentile | one-sided p for attenuation |
|---|---|---|---|---|---|
| Sharon | 0.0904 | 0.0891 | **1.02** | 52.1 | **0.52** |
| Yi | 0.1901 | 0.3155 | **0.58** | 4.4 | **0.044** |

### Against a fair comparator: the other lysine-modifying chromatin enzymes

Comparing to all ~19,000 genes is biased toward finding no attenuation, because
most background genes are not expressed in the screen cell line and sit at the
|effect| floor by construction. The closest matched comparator is the KDM, KAT,
KMT, DNMT and BRD families: same compartment, same class of catalytic activity
on the same substrates, no claimed dual pro/antiviral role.

| screen | 18 enzymes | all 48 chromatin enzymes | ratio | MW p |
|---|---|---|---|---|
| Sharon | 0.0904 | 0.1213 | 0.745 | 0.30 |
| Yi | 0.1901 | 0.2680 | 0.709 | 0.85 |

Consistent direction, roughly a 0.72 ratio in both screens, significant in
neither. Note that in Yi the median ratio (0.71) and the Mann-Whitney p (0.85)
disagree, because HDAC8 (1.03) and SIRT5 (1.21) are large outliers that lift the
rank distribution while the median stays low.

### Dual-role subset HDAC1, HDAC6, HDAC8 (n = 3)

Sharon: median 0.1339, matched-null percentile **79.1**, which is the *opposite*
of the prediction. Yi: median 0.1787, percentile 21.1, p = 0.21. At n = 3 no
result is informative in either direction, and this subset should not be
reported as a test.

### Power, which is the number that settles it

| if true \|effect\| were this fraction of matched background | power at α = 0.05 |
|---|---|
| 90% | 6% (Sharon), 10% (Yi) |
| 80% | 14%, 20% |
| 70% | **31%** |
| 60% | 57% |
| 50% | 87% |

With n = 18 the test has 31% power against a 30% true attenuation. A null result
cannot refute the model and a nominal result cannot support it. This is not a
precise null like Gate 3's; it is an underpowered one.

---

## 5. Why Yi's nominal attenuation is not cancellation

This is the decisive control. Olfactory receptors and keratins are not expressed
in A549 or HEK293 and cannot produce an influenza phenotype. If the 18 enzymes
sit *below* them, the apparent attenuation cannot be cancellation of real
opposing biology, because there is no biology at all in the comparator.

| screen | 18 enzymes | olfactory receptors (n≈250) | keratins (n=50) | ratio to OR |
|---|---|---|---|---|
| Sharon | 0.0904 | 0.0708 | 0.1051 | **1.28** |
| Yi | 0.1901 | 0.3187 | 0.3161 | **0.60** |

In Yi the 18 enzymes have 60% of the |effect| of genes that cannot have an
effect. Cancellation cannot produce that. Measurement precision can. So Yi's
p = 0.044 is a technical artefact, and the Sharon result (ratio 1.28 against the
same comparator) is the one consistent with the matched test.

---

## 6. Neither screen measures what the test requires

Core-essential gene families must deplete in any proliferation-coupled screen.
Centred LFC medians:

| gene family | Sharon | Yi |
|---|---|---|
| ribosomal RPL* | −0.055 | **+0.261** |
| ribosomal RPS* | +0.031 | +0.102 |
| proteasome PSMA/B* | −0.057 | +0.002 |
| eIF* | −0.013 | +0.063 |
| keratins (non-essential) | −0.089 | +0.022 |
| olfactory receptors (not expressed) | +0.027 | −0.165 |

Ribosomal and proteasome genes are indistinguishable from keratins and olfactory
receptors in Sharon, and in Yi the ribosomal genes move in the *wrong*
direction. Correlation with DepMap Chronos across the 32 genes streamed:
r = **−0.159** (Sharon), **+0.070** (Yi), where a dropout-sensitive screen must
give a clear positive.

Cross-screen Spearman correlation of centred LFC over **18,418 shared genes:
rho = −0.0106**, p = 0.15. For the top 200 genes by |Sharon effect|,
rho = −0.039. The 18 enzymes give rho = −0.420 (p = 0.064, 4.4th percentile of a
random-18 null), which with several gene sets tested is not interpretable.

These screens therefore agree on essentially nothing outside a handful of very
strong hits. Both recover SLC35A1, and that is about the extent of it. Their
gene-level effect sizes are not a usable currency for meta-analysis, and no
amount of modelling fixes that.

### A conceptual objection, separate from the data

Cancellation within a single screen requires one gene to exert opposing pro- and
antiviral effects in the *same* cell type, strain, readout and timepoint. The
manuscript's dual-role evidence is assembled across different cell systems,
strains and assays. A gene with a single net phenotype in one condition has
nothing to cancel against. Before any version of this test is attempted, Section
4.4 needs to state whether the claim is about within-condition opposition, which
is what a screen measures, or about across-condition divergence, which is what
the literature actually shows. As written, the prediction and the assay are not
matched.

---

## 7. DepMap Chronos: the one clean result, and it is useful

DepMap 24Q4 Public, 1,178 cell lines, 126 of Lung lineage. Chronos: 0 = no
effect, about −1 = median known-essential gene; "dependent" is Chronos < −0.5.

| gene | mean | median | min | % lines dependent | lung mean | lung % dep |
|---|---|---|---|---|---|---|
| **HDAC3** | **−0.934** | −0.934 | −2.091 | **87.4%** | −0.815 | **81.0%** |
| SIRT7 | −0.181 | −0.182 | −1.033 | 3.3% | −0.154 | 1.6% |
| HDAC5 | −0.160 | −0.161 | −0.591 | 0.6% | −0.173 | 0.0% |
| HDAC1 | −0.155 | −0.133 | −2.360 | 4.0% | −0.148 | 2.4% |
| SIRT4 | −0.151 | −0.146 | −0.683 | 0.6% | −0.143 | 0.0% |
| HDAC7 | −0.107 | −0.092 | −1.788 | 2.5% | −0.116 | 1.6% |
| HDAC8 | −0.093 | −0.078 | −0.884 | 2.5% | −0.072 | 0.8% |
| HDAC4 | −0.078 | −0.067 | −0.882 | 1.5% | −0.135 | 4.8% |
| SIRT2 | −0.069 | −0.060 | −0.852 | 0.6% | −0.087 | 0.8% |
| HDAC2 | −0.060 | −0.036 | −1.877 | 2.8% | −0.037 | 2.4% |
| **HDAC6** | **−0.056** | −0.056 | −0.496 | **0.0%** | −0.075 | **0.0%** |
| HDAC11 | −0.023 | −0.018 | −0.810 | 0.2% | −0.028 | 0.0% |
| HDAC10 | −0.002 | −0.003 | −0.414 | 0.0% | +0.003 | 0.0% |
| SIRT3 | +0.028 | +0.025 | −0.642 | 0.3% | +0.054 | 0.8% |
| SIRT5 | +0.066 | +0.063 | −0.554 | 0.2% | +0.073 | 0.0% |
| SIRT1 | +0.079 | +0.085 | −0.769 | 0.4% | +0.072 | 0.8% |
| HDAC9 | +0.102 | +0.103 | −0.272 | 0.0% | +0.105 | 0.0% |
| SIRT6 | +0.113 | +0.118 | −0.435 | 0.0% | +0.133 | 0.0% |

Calibration: RAN −3.933 (100%), RPL3 −2.533 (100%), EIF4A3 −2.294 (100%),
PSMA1 −2.254 (100%); KRT36 −0.025 (0.1%). IAV screen hits: ATP6V1F −1.124
(94.0%), WDR7 −0.770 (75.7%), SLC35A1 −0.109 (5.1%), CYTH2 −0.041 (0.1%).
Gate 5 set: GPKOW −1.016 (98.1%), PPP6C −0.398 (34.7%), CTTN −0.215 (3.7%),
KPNA6 −0.189 (2.9%), STAT1 −0.007 (0.0%).

Three things follow, and they are the usable output of Gate 4.

**HDAC3 pan-essentiality is a structural confound for viability-readout IAV
screens.** Han, Song and Yi all used cell survival. A gene whose knockout is
lethal in 87% of cell lines, and 81% of lung lines, cannot score as protective
against influenza-induced death: its sgRNAs drop out whether or not virus is
present. HDAC3 is therefore systematically unscoreable in exactly the design
three of the ten screens used. Consistent with this, HDAC3's only nominal signal
anywhere is in Sharon (neg p 0.00175, rank 251), which is a GFP-reporter screen
and not a viability screen.

**For the other 17, failure to score is not dropout.** They are non-essential,
at most 4% of lines dependent, so they are perfectly scoreable and simply do not
score. This weakens the "cancellation masks a real effect" reading rather than
supporting it, because both directions were measurable and neither appeared.

**HDAC3 versus HDAC6 is a quantitative basis for the target axis.** HDAC3 at
87.4% dependency against HDAC6 at 0.0% across 1,178 cell lines is a clean,
independent, citable reason why selective HDAC6 agents have a therapeutic window
and pan-HDAC or HDAC3-directed agents do not. This supports the manuscript's
existing target and domain argument with a hard number from a resource no
reviewer will dispute, and it does so without needing the cancellation model at
all.

---

## 8. Recommendation

Drop the cancellation test. It cannot be run: two usable screens, zero
cross-screen correlation, no essentiality signal in either, 31% power against a
30% effect, and the one nominal result attributable to precision. Reporting it
as a null would overstate what the data can say, and reporting Yi's p = 0.044 as
support would be worse.

Reframe Section 4.4 around two defensible statements instead.

First, **the 18 enzymes are completely covered and uniformly absent from
genome-wide IAV screen hits**, with exact ranks and FDRs now in hand from two
screens, and with non-essentiality in DepMap ruling out dropout as the
explanation for 17 of 18. That is a real, quantified negative, and it is
stronger than the hit-overlap tables currently in the literature.

Second, **HDAC3's pan-essentiality explains why one axis of the framework is
invisible to the dominant screen design**, and simultaneously gives the
therapeutic-window argument a quantitative anchor. This is the result to
promote.

Before writing either, Section 4.4 needs to say whether its claim is about
within-condition opposition or across-condition divergence, because the two
imply different tests and only the second matches the evidence that exists.

---

## 9. Limitations

**Two screens is two screens.** If full MAGeCK gene summaries for Han, Song or
Yi's replicates can be obtained from the authors, the matched test becomes worth
rerunning, though the power calculation above will not improve much: n = 18 is
fixed by biology, not by the number of screens.

**Matching was on sgRNA count only.** DepMap Chronos was streamed for 32 genes,
not genome-wide, so the essentiality decile could not enter the matched
permutation. Genome-wide Chronos plus A549 expression would allow proper
matching, and the olfactory-receptor control in Section 5 suggests the missing
covariate is baseline sgRNA representation rather than essentiality.

**Sharon is HEK293SF, not a respiratory cell**, and uses a GFPΔHA reporter virus
with a single-cycle readout. Yi is A549 with H7N9 and lethal selection. Neither
matches the systems in which the HDAC literature was generated.

**Yi's selection was severe.** The library median LFC of −5.29 means
approximately 97% of sgRNA representation was lost, so gene-level estimates
carry heavy bottleneck noise. This is the most likely source of both the absent
essentiality signal and the spurious attenuation.

**Multiple testing across the gate.** Naive, matched and chromatin-comparator
tests were run on two screens, plus a dual-role subset and a reproducibility
analysis. The single nominal result (Yi, one-sided p = 0.044) does not survive
any correction for that, and was independently explained in Section 5.
