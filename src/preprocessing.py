from pathlib import Path

import joblib
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
FEATURE_PATH = BASE_DIR / "models" / "feature_columns.pkl"
feature_columns = joblib.load(FEATURE_PATH)


def preprocess_input(form):

    # Create dataframe with all features initialized to 0
    data = pd.DataFrame(
        [[0] * len(feature_columns)],
        columns=feature_columns
    )

    # Numerical Features
    data["Tenure Months"] = float(form["tenure"])
    data["Monthly Charges"] = float(form["monthly_charges"])
    data["Total Charges"] = float(form["total_charges"])

    # Gender
    if form["gender"] == "Male":
        data["Gender_Male"] = 1

    # Senior Citizen
    if form["senior"] == "Yes":
        data["Senior Citizen_Yes"] = 1

    # Partner
    if form["partner"] == "Yes":
        data["Partner_Yes"] = 1

    # Dependents
    if form["dependents"] == "Yes":
        data["Dependents_Yes"] = 1

    # Phone Service
    if form["phone"] == "Yes":
        data["Phone Service_Yes"] = 1

    # Multiple Lines
    if form["multiple_lines"] == "No phone service":
        data["Multiple Lines_No phone service"] = 1

    elif form["multiple_lines"] == "Yes":
        data["Multiple Lines_Yes"] = 1

    # Internet Service
    if form["internet"] == "Fiber optic":
        data["Internet Service_Fiber optic"] = 1

    elif form["internet"] == "No":
        data["Internet Service_No"] = 1

    # Online Security
    if form["online_security"] == "No internet service":
        data["Online Security_No internet service"] = 1

    elif form["online_security"] == "Yes":
        data["Online Security_Yes"] = 1

    # Online Backup
    if form["online_backup"] == "No internet service":
        data["Online Backup_No internet service"] = 1

    elif form["online_backup"] == "Yes":
        data["Online Backup_Yes"] = 1

    # Device Protection
    if form["device_protection"] == "No internet service":
        data["Device Protection_No internet service"] = 1

    elif form["device_protection"] == "Yes":
        data["Device Protection_Yes"] = 1

    # Tech Support
    if form["tech_support"] == "No internet service":
        data["Tech Support_No internet service"] = 1

    elif form["tech_support"] == "Yes":
        data["Tech Support_Yes"] = 1

    # Streaming TV
    if form["streaming_tv"] == "No internet service":
        data["Streaming TV_No internet service"] = 1

    elif form["streaming_tv"] == "Yes":
        data["Streaming TV_Yes"] = 1

    # Streaming Movies
    if form["streaming_movies"] == "No internet service":
        data["Streaming Movies_No internet service"] = 1

    elif form["streaming_movies"] == "Yes":
        data["Streaming Movies_Yes"] = 1

    # Contract
    if form["contract"] == "One year":
        data["Contract_One year"] = 1

    elif form["contract"] == "Two year":
        data["Contract_Two year"] = 1

    # Paperless Billing
    if form["paperless"] == "Yes":
        data["Paperless Billing_Yes"] = 1

    # Payment Method
    if form["payment"] == "Credit card (automatic)":
        data["Payment Method_Credit card (automatic)"] = 1

    elif form["payment"] == "Electronic check":
        data["Payment Method_Electronic check"] = 1

    elif form["payment"] == "Mailed check":
        data["Payment Method_Mailed check"] = 1

    return data