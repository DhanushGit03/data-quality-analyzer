import pandas as pd
from data_profiler import profile_data
from visualizer import plot_missing, plot_outliers

def main():
    data_path = 'sample_data/example.csv'
    try:
        df = pd.read_csv(data_path)
        print("\n📄 Data loaded successfully.\n")
    except FileNotFoundError:
        print(f"❌ File not found: {data_path}\nPlease make sure the data file exists.")
        return
    except Exception as e:
        print(f"❌ An error occurred while loading the data: {e}")
        return

    profile = profile_data(df)

    print("📊 Summary Statistics:\n")
    print(profile['summary'])

    print("\n🧩 Missing Values:\n")
    print(profile['missing'])

    print("\n🚨 Outliers Found:\n")
    for column, outlier_df in profile['outliers'].items():
        if not outlier_df.empty:
            print(f"🔹 {column}: {len(outlier_df)} outliers")
            print(outlier_df[[column]])
        else:
            print(f"✅ {column}: No outliers")

    plot_missing(df)
    plot_outliers(profile)

if __name__ == "__main__":
    main()