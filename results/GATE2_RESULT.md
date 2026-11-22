# Gate 2 Result: Independent PA-X Transcript Depletion (GSE120183)

Source dataset: GEO GSE120183 (Gaucherand et al., Cell Rep 2019; A549 cells, A/PR/8/1934 WT vs. PA(fs) and PA(ΔX) mutants, ~9,500 quantified transcripts).  
Script: `scripts/gate2_paxcheck.py`

## Summary of PA-X-Specific Effects (log2 ratio: WT − PA-X-null)

- Background median: −0.39 (PA(fs)), −0.48 (PA(ΔX))
- **HDAC1:** −0.89 (12.3rd pctile, PA(fs)); −1.32 (5.3rd pctile, PA(ΔX)) — strong PA-X-dependent depletion
- **HDAC4:** −1.06 (6.9th pctile, PA(fs)) — strong PA-X-dependent depletion
- **HDAC6:** −0.88 (12.4th pctile, PA(fs)); −1.17 (8.8th pctile, PA(ΔX)) — strong PA-X-dependent depletion
- **HDAC8:** −0.74 (19.7th pctile, PA(fs)); −1.03 (13.8th pctile, PA(ΔX)) — PA-X-dependent depletion
- **SIRT1:** +1.06 (99.1st pctile, PA(fs)); +0.32 (93.2nd pctile, PA(ΔX)) — opposite direction (rules out PA-X mRNA decay)
