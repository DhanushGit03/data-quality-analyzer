import pandas as pd
from sqlalchemy import create_engine

def validate_with_sql(df, table_name, db_url):
    engine = create_engine(db_url)
    sql_df = pd.read_sql(f"SELECT * FROM {table_name};", engine)
    return df.equals(sql_df)