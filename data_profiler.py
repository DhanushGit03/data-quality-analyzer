import pandas as pd

def profile_data(df):
    summary = df.describe(include='all')
    missing = df.isnull().sum()
    outliers = {}
    for column in df.select_dtypes(include=['float64', 'int64']).columns:
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        outlier_rows = df[(df[column] < Q1 - 1.5 * IQR) | (df[column] > Q3 + 1.5 * IQR)]
        outliers[column] = outlier_rows
    return {
        'summary': summary,
        'missing': missing,
        'outliers': outliers
    }