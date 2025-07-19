import pandas as pd
from pandas_profiling import ProfileReport

def generate_profile(df, output_file="data/processed/profile.html"):
    profile = ProfileReport(df, title="Data Quality Report", explorative=True)
    profile.to_file(output_file=output_file)
