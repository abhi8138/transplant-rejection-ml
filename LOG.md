## 2026-10-19
- Downloaded GSE150059 series matrix; loaded with custom read_series_matrix() in src/geo.py.
- Exploratory PCA on top 5,000 variance probes.
- Issue: kernel crashed at PCA (BLAS conflict on Windows). Fixed by rebuilding env with OpenBLAS.
- Next: check label columns, decide prediction target, then DE and modelling.

## 2026-10-20
- Added a cohort table of MMDx diagnosis counts.
- Differential expression (limma) in notebooks/03_differential_expression.ipynb, comparing each MMDx group against a reference group.
- InMoose needed Microsoft C++ Build Tools to install on Windows; switched to python-limma (pure Python, import name pylimma).
- Gene symbols from the platform (GPL) annotation via GEOparse; the series matrix file has no probe annotation (GEOquery fetches it separately in R).
- Volcano plots for all comparisons in one figure, top 10 genes labelled with adjustText (ggrepel equivalent).
- Next: check python-limma results against R limma on one comparison; consider a single limma model with all groups; decide the modelling target (MMDx calls derive from the same expression data).

## 2026-10-27
- Notebook 04: penalised logistic regression (glmnet equivalent) for pairwise MMDx comparisons against NR Normal, alpha = 0.5 (elastic net) and 1 (lasso).
- Design: repeated stratified 5-fold CV (5 repeats) via cross_validate; inner 5-fold CV chooses C (lambda.min equivalent); top 1,000 genes selected inside each training fold.
- Outputs: per-fold AUC, lambda, number of genes; ROC curves with pooled out-of-fold AUC and bootstrap 95% CI.
- Moved from a manual grid + per-row function (R pmap style) to scikit-learn's cross_validate.
- R habits caught: T instead of True.
- Result: AUCs near 1. Expected given MMDx circularity, but not yet verified.
- Next: check for repeated biopsies per patient (StratifiedGroupKFold if a patient ID exists); shuffled-label control (expect AUC ~0.5); look for independent outcomes (histology, LVEF, graft loss) in the metadata.