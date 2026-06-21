import pandas as pd

df = pd.read_csv("data_extraction/raw_data/customer_data.csv")

print("=" * 50)
print("DATA VALIDATION REPORT")
print("=" * 50)
print()

print("Shape: ", df.shape)
print()

print("Columns: " ,df.columns)
print()

print("Missing Values: ",df.isnull().sum())
print()

print("\nDuplicate Rows: ", df.duplicated().sum())
print()

print("\nData Types: ", df.dtypes)