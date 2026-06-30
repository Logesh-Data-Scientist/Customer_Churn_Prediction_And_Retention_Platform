import joblib

feature_columns = joblib.load(r"C:\Users\Hey!\OneDrive\Desktop\Customer churn prediction & retention Platform\models\feature_columns.pkl")

print("Number of Features:", len(feature_columns))

for i, feature in enumerate(feature_columns, 1):
    print(f"{i}. {feature}")