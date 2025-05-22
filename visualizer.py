import matplotlib.pyplot as plt

def plot_missing(df):
    missing = df.isnull().sum()
    missing[missing > 0].plot(kind='bar')
    plt.title('Missing Values per Column')
    plt.show()

def plot_outliers(profile):
    outliers = profile['outliers']
    pd.Series(outliers).plot(kind='bar')
    plt.title('Outliers per Numeric Column')
    plt.show()