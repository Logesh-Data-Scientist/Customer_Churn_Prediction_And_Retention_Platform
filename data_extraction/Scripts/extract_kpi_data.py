import pandas as pd

from db_connection import get_engine

engine = get_engine()

with open(r"C:\Users\Hey!\OneDrive\Desktop\Customer churn prediction & retention Platform\data_extraction\queries\kpi_data.sql", "r") as file:
    query = file.read()

df = pd.read_sql(query, engine)

print(df)

df.to_csv(
    "data_extraction/raw_data/kpi_data.csv",
    index=False
)

print("KPI Data Extracted Successfully")