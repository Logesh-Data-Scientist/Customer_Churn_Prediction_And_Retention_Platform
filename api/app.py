"""
FastAPI application for Customer Churn Prediction Platform.
"""

from fastapi import FastAPI, HTTPException
import pandas as pd

from src.predictor import ChurnPredictor

app = FastAPI(
    title="Customer Churn Prediction API",
    description="Production API for Customer Churn Prediction",
    version="1.0.0"
)

# Load predictor once during startup
predictor = ChurnPredictor()


@app.get("/")
def home():
    """
    Health check endpoint.
    """
    return {
        "status": "Running",
        "message": "Customer Churn Prediction API is running successfully."
    }


@app.post("/predict")
def predict(customer_data: dict):
    """
    Predict customer churn.
    """

    try:

        # Convert JSON to DataFrame
        df = pd.DataFrame([customer_data])

        # Predict
        result = predictor.predict(df)

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )