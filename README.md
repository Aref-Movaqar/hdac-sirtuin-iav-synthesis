# Target, Domain, and Stage: A Three-Axis Framework and Quantitative Synthesis of HDAC and Sirtuin Function in Influenza A Virus Infection

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24441667.svg)](https://doi.org/10.5281/zenodo.24441667)

This repository contains the curated evidence matrix, reproducible analysis scripts, intermediate outputs, and publication-ready figures supporting the manuscript:

> **Movaqar, A., & Amel Jamehdar, S.** *Target, Domain, and Stage: A Three-Axis Framework and Quantitative Synthesis of HDAC and Sirtuin Function in Influenza A Virus Infection.*

---

## Repository Structure

* `data/` — Curated evidence matrix (`Supplementary_Evidence_Matrix_v2.csv`, Supplementary Table S1: 47 evidence units across 12 research programmes) and intermediate PA-X cut-site tables (`cut_level.tsv`, `exon_level.tsv`, `tx_level.tsv`).
* `scripts/` — Python scripts implementing the sequence alignment (`gate1_align.py`), independent PA-X transcript depletion check (`gate2_paxcheck.py`), and transcriptome-wide PA-X cut-site conditional logistic regression (`gate3_analysis.py`).
* `results/` — Structured audit reports (`GATE1_RESULT.md` through `GATE6_RESULT.md`) summarizing all six quantitative verification gates.
* `figures/` — High-resolution (300 DPI) figures (`.png`) generated directly from the quantitative verification pipelines (Figures 5, 6, 8, and 10).

---

## Summary of Quantitative Verification Gates

| Gate | Scope | Public Dataset(s) | Key Finding |
| :--- | :--- | :--- | :--- |
| **Gate 1** | Viral sequence conservation & PA-X frameshift translation | NCBI RefSeq/GenBank (7 IAV strains: H1N1, H5N1, H7N7, H7N9) | PA K664 (±5 aa) and NP K229 (±5 aa) are 100% invariant; NP-K103 sequence variation does not explain HDAC1 divergence; 2009 pH1N1 carries a truncated 232-aa PA-X. |
| **Gate 2** | Independent PA-X transcript depletion | GEO `GSE120183` (Gaucherand et al., 2019) | Supports PA-X-dependent depletion of `HDAC4` (6.9th pctile), `HDAC6` (8.8th–12.4th pctile), `HDAC1` (5.3rd–12.3rd pctile), and `HDAC8` (across 8/18 quantified enzymes); rules out PA-X mRNA decay for `SIRT1` (93.2nd–99.1st pctile, opposite direction). |
| **Gate 3** | Transcriptome-wide PA-X cut-site architecture & EJC footprint | GEO `GSE207253` (Gaucherand et al., 2023) + hg38 RefSeq | Within-transcript conditional logistic regression (858 strata) refutes terminal-exon enrichment after adjusting for exon length (OR = 1.04, *p* = 0.76); first exons are depleted (OR = 0.66, *p* = 0.0022); no EJC-footprint depletion at 20–25 nt (ratio 0.92). |
| **Gate 4** | Genome-wide IAV CRISPR screens & gene essentiality | DepMap `24Q4 Public` (1,178 lines); Sharon et al. (2020); Yi et al. (2022) | `HDAC3` is pan-essential (87.4% all lines; 81.0% lung lines), confounding viability screens; 17/18 other enzymes are non-essential (`HDAC6` = 0.0%); 0/18 reach FDR significance in full-table IAV CRISPR screens. |
| **Gate 5** | Independent quantitative IAV proteomics | Pichlmair (`PXD047063`); Bogdanow (`PXD011321`); Krogan (2023) | Replicates NS1-independent `HDAC2` destabilization (Δd₀ = +0.303, *p* = 8.9 × 10⁻³³); shows no accelerated whole-protein turnover for `HDAC4`/`HDAC6` in HeLa; reveals strain/cell-type sign reversal for `HDAC1`. |
| **Gate 6** | Literature evidence structure & confounding | `Supplementary_Evidence_Matrix_v2.csv` (n = 30 direct IAV units) | Single-programme concentration (53.3% of units; 100% of Tier-1 antagonism); statistically significant confounding after Bergsma bias correction (10,000 permutations) for stage vs. readout (V_corr = 0.557, *p* = 0.0025), lab vs. stage (V_corr = 0.497, *p* = 0.023), and programme vs. enzyme (V_corr = 0.388, *p* = 0.050). |

---

## Requirements

Analyses were executed in Python 3.10+ using standard scientific libraries:

```bash
pip install numpy pandas scipy statsmodels matplotlib biopython
