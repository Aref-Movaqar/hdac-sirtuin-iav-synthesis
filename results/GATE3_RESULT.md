# Gate 3 result: the splicing-coupled terminal-exon accessibility model fails

Run 21 November 2026. Data: GEO **GSE207253**, transcriptome-wide PA-X cut sites
mapped by 5′ RACE-seq in A549 cells (Gaucherand & Gaglia, *Nat Microbiol* 2023).
Annotation: UCSC refGene, hg38, 88,819 transcripts.

Build confirmed empirically: 89.9 percent of cut sites fall inside the span of
the gene the file itself names under hg38, against 8.2 percent under hg19.

Cut sites: 1,361 in the concatenated set, 592 in the shared (reproducible) set.
Assigned to an exon of an annotated transcript: 1,179 and 526 respectively. The
remainder are intronic or in genes absent from refGene.

## Verdict: NO-GO

Three independent tests reject the model, and one of them rejects it in the
direction opposite to its prediction.

---

## 1. Terminal-exon enrichment is entirely an exon-length artefact

Primary design: conditional (stratified) logistic regression with transcript as
the stratum. Within a transcript, expression, transcript length, GC content,
3′ UTR length and detection bias are all constants and cannot contribute. The
only covariate that must still be modelled is exon length, because terminal
exons are systematically far longer: median 1,376 nt against 128 nt for internal
exons, an 11-fold difference.

858 informative strata, 12,006 exons, 1,029 exons carrying a cut.

| model | predictor | β | SE | OR | 95% CI | p |
|---|---|---|---|---|---|---|
| terminal only | is_terminal | +1.7959 | 0.0747 | **6.025** | 5.204, 6.975 | <1e−100 |
| + log(length) | is_terminal | +0.0410 | 0.1318 | **1.042** | **0.805, 1.349** | **0.76** |
| | log(length) | +0.8224 | 0.0524 | 2.276 | 2.054, 2.522 | <1e−50 |
| + first exon | is_terminal | −0.1189 | 0.1423 | 0.888 | 0.672, 1.174 | 0.40 |
| | log(length) | +0.8656 | 0.0547 | 2.376 | 2.135, 2.645 | <1e−50 |
| | is_first | −0.4177 | 0.1363 | 0.659 | 0.504, 0.860 | 0.0022 |

Unadjusted, terminal exons look spectacularly enriched, OR 6.0. Adjusted for
length, the effect vanishes: OR 1.04 with a confidence interval of 0.81 to 1.35.
That interval is tight enough to exclude even a 1.4-fold enrichment, so this is
not an underpowered null. It is a precise null.

The shared, more stringent set reproduces it exactly: OR 7.18 unadjusted,
then **1.17 [0.81, 1.67], p = 0.40** once length is in the model, and
0.97 [0.66, 1.44] with first-exon status added.

First exons are genuinely depleted, OR 0.66, which is the only positional effect
that survives adjustment.

**Per-nucleotide uniformity.** If cuts were distributed uniformly along exonic
sequence, the log-length coefficient would be 1.0. It is 0.82 [0.72, 0.93],
significantly below 1 in the concatenated set (p = 0.0007) and not distinguishable
from 1 in the shared set (0.87 [0.72, 1.02], p = 0.09). So cut density is
approximately uniform per nucleotide, if anything slightly sub-linear in exon
length. There is no per-nucleotide accessibility advantage to terminal exons.

---

## 2. Between transcripts, terminal-exon length predicts cutting in the wrong direction

57,408 multi-exon coding transcripts, 789 (1.37 percent) carrying at least one cut.

| model | predictor | β | SE | OR | 95% CI | p |
|---|---|---|---|---|---|---|
| 3′UTR only | log(3′UTR length) | −0.0404 | 0.0296 | 0.960 | 0.906, 1.018 | 0.17 |
| terminal only | log(terminal exon) | −0.0880 | 0.0359 | 0.916 | 0.853, 0.983 | 0.014 |
| both | log(terminal exon) | −0.3416 | 0.1087 | **0.711** | 0.574, 0.879 | 0.0017 |
| | log(3′UTR length) | +0.2269 | 0.0924 | 1.255 | 1.047, 1.504 | 0.014 |
| full | log(terminal exon) | −0.3731 | 0.1184 | **0.689** | 0.546, 0.868 | 0.0016 |
| | log(3′UTR length) | +0.1625 | 0.0923 | 1.176 | 0.982, 1.410 | 0.079 |
| | log(transcript length) | +0.2032 | 0.1124 | 1.225 | 0.983, 1.527 | 0.071 |
| | exon count | +0.0082 | 0.0035 | 1.008 | 1.001, 1.015 | 0.020 |

The model predicts that long terminal exons should attract PA-X. They repel it:
every specification gives an odds ratio below 1, and conditioning on 3′ UTR
length makes the negative association stronger, not weaker. The only positive
architectural term is 3′ UTR length, which is the covariate the manuscript treats
as the thing terminal-exon status is supposed to beat.

Full-model pseudo-R² is 0.0046. Transcript architecture explains essentially
nothing about which transcripts PA-X cuts.

This analysis does **not** control baseline expression, and cut-site detection
requires expression, so these coefficients should be read as a direction check
rather than as effect estimates. The direction is unambiguous and the primary
within-transcript analysis does not depend on it.

---

## 3. Cut sites are junction-proximal, not junction-distal, and the EJC footprint shows no depletion

Distance from each cut to the nearest exon–exon junction, against a null of
length-weighted random exonic positions drawn from the same transcripts, 20
draws per observed cut.

| distance to nearest junction | observed | null | ratio |
|---|---|---|---|
| 0–10 nt | 6.8% | 6.6% | 1.02 |
| 10–20 nt | 9.7% | 6.7% | **1.44** |
| **20–25 nt (EJC footprint)** | **3.1%** | **3.4%** | **0.92** |
| 25–50 nt | 18.6% | 15.8% | 1.18 |
| 50–100 nt | 19.8% | 14.6% | 1.35 |
| 100–500 nt | 16.9% | 22.9% | 0.74 |
| >500 nt | 25.2% | 30.0% | 0.84 |

Median observed distance 72 nt against 122 nt expected. Mann-Whitney two-sided
p = 0.00015.

Two things follow. There is **no depletion in the 20 to 24 nt window** where
Section 5.3 places exon junction complex deposition: the ratio is 0.92, which is
nothing. And cuts are **closer** to junctions than chance, with enrichment at 10
to 20 nt and 50 to 100 nt and depletion beyond 100 nt. The model predicts the
reverse.

---

## 4. HDAC4 and HDAC6 carry no mapped cut site; cortactin does

Among the 998 genes with at least one cut site in the concatenated set, none of
the eleven HDACs or seven sirtuins appears except **SIRT7**. **CTTN (cortactin)**
does appear.

Read this cautiously: 5′ RACE-seq is not saturating, 998 genes is a small
fraction of the transcriptome, and absence is weak evidence. But it sits
awkwardly beside Gate 2, where HDAC4 and HDAC6 were among the most
PA-X-dependently depleted transcripts in the GSE120183 panel. The two results
together say that these transcripts are lost in a PA-X-dependent way without a
detectable cut site in this assay, which points to detection limits, indirect
loss, or cleavage below the assay's sensitivity.

---

## 5. Confounds and limitations

**Transcript assignment is heuristic.** The median cut has 2 candidate
transcripts. I preferred the transcript whose gene symbol matches the file's own
annotation, then the one with most exons, then the longest exonic length.
Sensitivity to that choice has not been formally tested, and should be before
publication. Note that the heuristic favours multi-exon transcripts, which if
anything biases *toward* finding internal-exon cuts, that is, against the result
reported here being an artefact of transcript choice.

**Detection is expression-dependent** in both the cut-site and the
between-transcript analyses. The within-transcript design is immune to this.

**The junction-distance null** controls transcript identity and exonic length but
not local sequence composition. A dinucleotide-preserving null would be stronger
and is the obvious next refinement if this analysis is reported.

**182 of 1,361 cuts were unassignable** to an annotated exon. If PA-X cut
preferentially in unannotated terminal regions, excluding them could matter,
though it is hard to see how that would rescue the model.

**Cells are Xrn1-deficient A549** by design, so cut sites accumulate. Whether
the same positional distribution holds in Xrn1-competent cells is untested.

---

## 6. What this means for the manuscript

The splicing-coupled accessibility model has to go. It was the manuscript's
most ambitious original claim, it made a specific transcriptome-wide prediction,
the prediction has now been tested against the right dataset, and it failed three
ways including one reversal of sign. Section 5.3, Table 3's exon-context column,
Figure 4B and Question 5 all rest on it.

What survives, and it is not nothing:

- The HDAC4 and HDAC6 transcripts **are** PA-X-dependently depleted, confirmed in
  an independent laboratory's data (Gate 2). The phenomenon is real; the proposed
  mechanism is not.
- The GCUG motif analysis stands as computed, with the corrected
  composition-matched null.
- The positional findings are themselves publishable: PA-X cuts approximately
  uniformly per exonic nucleotide, is depleted in first exons, is modestly
  junction-proximal, and shows no EJC-footprint depletion. That is a sharper
  description of PA-X target selection than currently exists in the manuscript,
  and it is a genuine, if negative, contribution.

The honest reframing is that transcript architecture does not explain PA-X target
selection, which redirects the question to what does. Gaucherand's own conclusion
was cut-site sequence preference. Our GCUG result says the motif is not
differentially accessible. Those two together suggest the determinant is neither
local structure nor exon architecture, which is a well-posed open question rather
than a failed chapter.
