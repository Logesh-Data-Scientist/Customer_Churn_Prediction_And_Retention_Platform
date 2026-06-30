from pathlib import Path

import joblib

from src.preprocessing import preprocess_input
from src.recommendation import get_risk, get_recommendation

BASE_DIR = Path(__file__).resolve().parents[1]
MODEL_PATH = BASE_DIR / "models" / "best_model.pkl"

model = joblib.load(MODEL_PATH)


def predict_customer(form):
    input_df = preprocess_input(form)

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    risk = get_risk(probability)
    recommendation = get_recommendation(risk)

    result = "Customer Will Churn"
    if prediction == 0:
        result = "Customer Will Stay"

    return {
        "prediction": result,
        "probability": round(probability * 100, 2),
        "risk": risk,
        "recommendation": recommendation,
    }