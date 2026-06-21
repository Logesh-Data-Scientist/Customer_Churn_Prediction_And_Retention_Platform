import pandas as pd
from db_connection import get_engine
engine = get_engine()

with open(r"C:\Users\Hey!\OneDrive\Desktop\Customer churn prediction & retention Platform\data_extraction\queries\customer_data.sql", "r") as file:
    query = file.read()

df = pd.read_sql(query, engine)

print(df.head())

print("\nRows:", len(df))
print("Columns:", len(df.columns))

df.to_csv(
    "data_extraction/raw_data/customer_data.csv",
    index=False
)

print("\nCustomer data extracted successfully")