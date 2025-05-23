import matplotlib.pyplot as plt
import pandas as pd

def plot_missing(df):
    missing = df.isnull().sum()
    missing = missing[missing > 0]
    if not missing.empty:
        missing.plot(kind='bar')
        plt.title('Missing Values per Column')
        plt.show()
    else:
        print("No missing values found.")

def plot_outliers(profile):
    outliers = profile['outliers']
    outlier_counts = {col: len(vals) if hasattr(vals, '__len__') else 0 for col, vals in outliers.items()}
    outlier_counts = {col: count for col, count in outlier_counts.items() if count > 0}
    if outlier_counts:
        pd.Series(outlier_counts).plot(kind='bar')
        plt.title('Outliers per Numeric Column')
        plt.ylabel('Number of Outliers')
        plt.show()
    else:
        print("No outliers found.")