import pandas as pd
import numpy as np

def profile_data(df):
    profile = {}
    profile['missing_values'] = df.isnull().sum()
    profile['duplicates'] = df.duplicated().sum()
    numeric_cols = df.select_dtypes(include=[np.number])
    outliers = {}
    for col in numeric_cols:
        zscores = (df[col] - df[col].mean()) / df[col].std()
        outliers[col] = (abs(zscores) > 3).sum()
    profile['outliers'] = outliers
    profile['summary'] = df.describe(include='all')
    return profile