import gzip, io
import pandas as pd

def read_series_matrix(path):
    """Return (expr, meta) from a GEO series matrix .txt.gz file."""
    expr = pd.read_csv(path, sep="\t", comment="!", index_col=0)
    lines = [l for l in gzip.open(path, "rt") if l.startswith("!Sample_")]
    meta = pd.read_csv(io.StringIO("".join(lines)), sep="\t", header=None, index_col=0).T
    return expr, meta.set_index("!Sample_geo_accession")