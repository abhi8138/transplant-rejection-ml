## 2026-10-19
- Downloaded GSE150059 series matrix; loaded with custom read_series_matrix() in src/geo.py.
- Exploratory PCA on top 5,000 variance probes.
- Issue: kernel crashed at PCA (BLAS conflict on Windows). Fixed by rebuilding env with OpenBLAS.
- Next: check label columns, decide prediction target, then DE and modelling.
