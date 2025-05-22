import pandas as pd
from data_profiler import profile_data
from visualizer import plot_missing, plot_outliers

df = pd.read_csv('sample_data/example.csv')
profile = profile_data(df)
print(profile['summary'])
plot_missing(df)
plot_outliers(profile)