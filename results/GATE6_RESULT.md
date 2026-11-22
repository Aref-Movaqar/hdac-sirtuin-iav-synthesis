# Gate 6 result: the variance partition is not identifiable, and the confounding structure is itself the finding

Run 21 November 2026. Deliverables: `Supplementary_Evidence_Matrix.tsv` and
`.csv` (48 evidence units, 26 columns), `crosstab.txt` (full contingency tables).

## Verdict: NO-GO on `brms` variance partitioning. GO on publishing the confounding structure as a quantitative result.

Four independent criteria fail, and one of them fails in a way no model can
repair. Against that, the structure that blocks the model is measurable, has
never been stated numerically for this field, and is worth a figure of its own.

---

## 1. The matrix

One row per **evidence unit**, defined as a single (enzyme, infection stage,
study) combination carrying a direction or an antagonism mechanism. 48 units,
11 enzymes, transcribed from Tables 1 and 4 and Sections 4 to 7, with
bibliographic and methodological fields merged from the primary papers via
Europe PMC (25 of 27 resolved; Nagesh 2017 and Zhang 2024 were rate-limited and
their author blocks were taken from the manuscript's own reference list).

Evidence tiers, which are new and do real work:

| tier | definition | n |
|---|---|---|
| **T1** | direct IAV experiment, genetic perturbation, viral-output readout, **and** a named viral driver | **6** |
| **T2** | direct IAV experiment with perturbation and readout, but no driver identified or mechanism inferred | **21** |
| **T3** | direct IAV experiment, descriptive or correlative readout only | **4** |
| **T4** | mechanism established in another virus or a non-infection system, carried to IAV by inference | 5 |
| **T5** | not peer reviewed (conference abstract) | 1 |
| **TG** | generated in this work from independent public data (Gates 1 to 5) | 11 |

The confounding analysis below uses the **31 T1 to T3 units** only. T4 units are
not IAV experiments, T5 is not peer reviewed, and the TG units were deliberately
drawn from independent laboratories, so including any of them would flatter the
crossing structure rather than describe the field.

Stage distribution across all 48: antagonism 19, signaling 12, replication 5,
entry 4, egress 2, in vivo 2, metabolic 2, not applicable 2.

The Gate 1 correction is carried: HDAC1 growth is recorded as **">3-fold at 24 h
and >6-fold at 48 h"**, not as a "3 to 6-fold" range.

---

## 2. The field is one research programme plus a long tail

31 direct IAV units, 13 research programmes.

| research programme | units | share |
|---|---|---|
| **Husain-programme** | **16** | **51.6%** |
| Helenius | 2 | 6.5% |
| Guo | 2 | 6.5% |
| Nencioni | 2 | 6.5% |
| He, Yamauchi, Matthias, Dai, Krämer, Huang, Zhang, Cristea, Liu | 1 each | 3.2% each |

"Husain-programme" collapses ref 14 (Husain first author, Cheung senior author)
with Husain's subsequent independent work, because for a confounding analysis
the research programme is the relevant unit. Reported separately, Husain as
senior author is 15 of 31 and Cheung is 1.

Two consequences are worth stating plainly.

**All six Tier-1 units come from the Husain programme.** Every piece of evidence
in this literature that combines a genetic perturbation, a viral-output readout
and a named viral driver is from one programme: HDAC4 (refs 22, three units),
HDAC6 (refs 14 and 47, two units) and cortactin (ref 48). There is no
independent Tier-1 replication of any antagonism mechanism in the published
record.

**Eight of ten antagonism-mechanism units are from that programme** (Guo 1,
Nencioni 1). And four enzymes have direct IAV evidence from **only** the Husain
programme: HDAC2 (n=3), HDAC4 (n=3), HDAC11 (n=2) and cortactin (n=1). Two more
rest on a single other programme each: SIRT2 (Nencioni, n=2) and SIRT3 (Liu,
n=1).

Crossing does exist where the phenotype is contested: HDAC6 has 6 programmes,
HDAC1 3, SIRT1 3, HDAC8 2. So the enzymes with independent replication are
precisely the ones whose direction is disputed, and the enzymes with a clean
single direction are precisely the ones with no independent replication. That
inversion is worth a sentence in the manuscript.

---

## 3. Stage, readout and laboratory are nearly the same variable

Lab × stage, counts:

| programme | antagonism | egress | entry | in vivo | metabolic | replication | signaling |
|---|---|---|---|---|---|---|---|
| **Husain** | **8** | (1 via ref 14) | 0 | 1 | 0 | 0 | **6** |
| Helenius | . | . | **2** | . | . | . | . |
| Yamauchi | . | . | 1 | . | . | . | . |
| Matthias | . | . | 1 | . | . | . | . |
| Krämer | . | 1 | . | . | . | . | . |
| Dai, He, Huang, Cristea, Guo | . | . | . | . | . | 1 each | . |
| Nencioni | 1 | . | . | . | 1 | . | . |
| Liu | . | . | . | . | 1 | . | . |
| Guo | 1 | . | . | . | . | 1 | . |
| Zhang | . | . | . | . | . | . | 1 |

The antagonism and signaling literature is the Husain programme. The entry
literature is the Helenius, Yamauchi and Matthias axis and contains no Husain
units at all. And the readouts track the same split: Husain uses western and
qPCR (8 units), titre (5) and reporters (2) and no imaging; Helenius and
Yamauchi use imaging and entry assays (3 of the field's 3 imaging units).

**This means the "infection timing" axis of the Three-Axis model is confounded
with laboratory and with assay.** The stage-dependence the manuscript describes
is real as a description of the literature, but a part of it that cannot be
quantified reflects which group studies which stage with which instrument. This
needs saying in Section 4, and it is a limitation the framework can absorb
honestly rather than one that undermines it.

Cramér's V across candidate grouping factors (31 units):

| pair | V | |
|---|---|---|
| lab vs **strain** | **0.886** | near-collinear |
| lab vs **stage** | **0.788** | near-collinear |
| lab vs **readout** | **0.770** | near-collinear |
| enzyme vs tier | 0.739 | |
| readout vs stage | 0.735 | |
| lab vs enzyme | 0.705 | |
| enzyme vs stage | 0.534 | |
| enzyme vs readout | 0.513 | |
| strain vs stage | 0.488 | |
| enzyme vs strain | 0.434 | |
| strain vs readout | 0.220 | |

---

## 4. Identifiability: four criteria, four failures

**(a) Too few labs with replication.** Only **4 of 14** labs contribute two or
more units (Husain 15, Helenius 2, Guo 2, Nencioni 2). Estimating a
between-laboratory variance needs roughly five or more such labs. With four, and
one of them holding half the data, τ_lab is a single-group estimate wearing a
hierarchical hat.

**(b) No crossing between lab and strain.** Exactly **one** laboratory (Husain)
uses more than one strain class, and that second class is "not reported". No
strain class other than "not reported" is used by more than two labs.

**(c) The design is disconnected.** The lab-strain bipartite graph has **3
connected components** (sizes 14, 2, 2) and the lab-enzyme graph has **4**
(sizes 16, 4, 2, 2). Effects in different components are not on a common scale
by construction, so a pooled variance has no meaning across them.

**(d) Lab and strain are perfectly confounded for the one contrast that
matters.** The HDAC1 direction reversal is the empirical anchor of the strain
axis:

| unit | direction | programme | strain class | tier |
|---|---|---|---|---|
| EU001 | pro-viral | Helenius | not reported | T2 |
| EU002 | pro-viral (association) | He | avian H5N1/H7N9 | T2 |
| EU003 | antiviral | Husain | human seasonal H1N1 | T2 |
| EU004 | antiviral (signaling) | Husain | not reported | T3 |

Labs reporting both directions: **none**. Strain classes carrying both
directions: only "not reported", which is not a strain class. **No laboratory
tested both strain classes and no strain class was tested by both
laboratories.** No model, however specified, can attribute the HDAC1 reversal to
strain rather than to laboratory. This is not a precision problem; it is a rank
deficiency in the design.

---

## 5. A fifth obstacle, independent of confounding: the effect sizes are not commensurable

Even with a perfectly crossed design the meta-regression could not be fitted,
because the reported effects are not on one scale. The matrix contains **nine
distinct effect-size scales**: fold-change in titre, percent reduction in
polypeptide, percent reduction in transcript, log10 growth, log2 fold-change,
percentile of a distribution, TCID50 or pfu units, Chronos score, and
unquantified. Table 1 as written puts ">4-fold growth", "-41% pSTAT1",
"-53% viperin" and "polypeptide -47%" in a single cell. These cannot be pooled,
and converting between them would require variance estimates that the primary
papers do not report.

Reporting completeness, across the 31 direct IAV units, as the manuscript
currently states them:

| field | reported | share |
|---|---|---|
| **MOI** | **1 / 31** | **3.2%** |
| cell system | 7 / 31 | 22.6% |
| strain | 7 / 31 | 22.6% |

MOI is stated for one unit in thirty-one. Since the manuscript's own Table 4
attributes the HDAC4 and HDAC6 magnitude ranges to "depending on cell/MOI" and
"depending on timepoint/MOI", the field is explicitly invoking a moderator it
does not report. That is a clean, checkable, citable observation about the
literature.

---

## 6. What to do instead

**Drop the brms variance partition.** It would produce numbers, and the numbers
would be artefacts of a rank-deficient design. A reviewer who checks the
crosstab will see it.

**Publish the crosstab.** Sections 2 to 5 above are a quantitative description
of a field's evidence base that nobody has written down: the share held by one
programme, the absence of independent Tier-1 replication, the collinearity of
stage with laboratory and assay, the 3.2% MOI reporting rate, and the nine
incompatible effect scales. This is the kind of result that makes a resource
paper useful rather than merely comprehensive, and it motivates the framework
instead of undercutting it: a three-axis organising scheme is the right response
to a literature that cannot be pooled, and now there is a measurement showing
why.

**Keep the matrix as the central supplementary asset.** With the tier column it
does real work: it separates the six Tier-1 units from the twenty-one Tier-2,
marks the five inferred-from-other-systems claims that the manuscript currently
carries in the same tables as IAV findings, and flags the one abstract-only
citation (ref 88).

**Three specific manuscript consequences:**

1. Section 4 should state that the timing axis is confounded with laboratory and
   readout, with the V values, rather than presenting stage-dependence as a
   purely biological ordering.
2. Table 1 should carry the evidence tier per row. Four enzymes currently read
   with the same confidence as HDAC4 while resting on a single programme with no
   Tier-1 unit.
3. The manuscript should report the MOI, cell system and strain gaps as a
   finding, and recommend minimum reporting standards for the field. That is a
   constructive contribution a review is well placed to make.

---

## 7. Limitations

**Unit definition is a judgement.** I counted one unit per (enzyme, stage,
study). Counting per figure panel or per experiment would change the absolute
numbers, though not the concentration: the Husain share is driven by that
programme covering six enzymes across antagonism and signaling, which no
recounting alters.

**Strain is under-recovered.** Europe PMC full text was unavailable for 23 of 25
resolved studies because of rate limiting, so strain, cell and MOI come from the
manuscript's own statements. Where the manuscript is silent the field is "NR
(not stated in ms)", never a guess. Reading the 27 primary papers directly would
fill much of this, and would likely strengthen the confounding result by
resolving some "not reported" strains into specific classes that remain
lab-specific. It would not create crossing that does not exist.

**Two author blocks unresolved.** Nagesh 2017 (ref 33) and Zhang 2024 (ref 45)
were rate-limited; ref 33's senior author is unambiguous from the manuscript's
reference list (Husain M) and ref 45 is a T4 unit excluded from the analysis.

**"Lab" is senior author.** Shared trainees, collaborations and moves between
groups are not captured. The Husain and Cheung case is handled explicitly, and
both groupings are reported.

**Cramér's V on sparse tables is upward-biased.** With 14 by 10 levels and 31
observations, V overstates association. The structural findings do not depend on
it: the disconnected components, the single multi-strain lab and the HDAC1
confounding are combinatorial facts, not statistical estimates.
