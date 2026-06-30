"""
Prediction module for the Customer Churn Prediction Platform.
"""
from src.recommendation import get_recommendation
from datetime import datetime
import pandas as pd

from src.config import (
    BEST_MODEL_PATH,
    MODEL_NAME,
    MODEL_VERSION,
)

from src.utils import load_pickle
from src.validation import validate_input
from src.preprocessing import preprocess_data
from src.logger import logger
from src.exceptions import PredictionError


class ChurnPredictor:
    """
    Customer Churn Prediction class.
    """

    def __init__(self):
        """
        Initialize the predictor by loading the trained model.
        """

        try:
            logger.info("Loading trained model...")

            self.model = load_pickle(BEST_MODEL_PATH)

            logger.info("Model loaded successfully.")

        except Exception as e:
            logger.error(f"Model loading failed: {e}")

            raise PredictionError(
                f"Unable to load trained model.\n{e}"
            )

    def predict(self, data: pd.DataFrame):
        """
        Predict customer churn.

        Parameters
        ----------
        data : pd.DataFrame
            Customer data.

        Returns
        -------
        dict
            Prediction result with probability and metadata.
        """

        try:
            logger.info("Prediction started.")

            # Step 1: Validate input
            validated_data = validate_input(data)

            # Step 2: Preprocess input
            processed_data = preprocess_data(validated_data)

            # Step 3: Prediction
            prediction = self.model.predict(processed_data)[0]

            # Step 4: Probability
            probability = self.model.predict_proba(processed_data)[0][1]

            # Step 5: Risk Level
            recommendation = get_recommendation(validated_data.iloc[0],probability)
            

            logger.info(
                f"Prediction completed successfully. "
                f"Prediction={prediction}, "
                f"Probability={probability:.4f}"
            )

            return {
    "prediction": (
        "Likely to Churn"
        if prediction == 1
        else "Not Likely to Churn"
    ),
    "churn_probability": round(float(probability) * 100, 2),
    "risk_level": recommendation["risk_level"],
    "customer_priority": recommendation["customer_priority"],
    "recommended_action": recommendation["recommended_action"],
    "business_reasons": recommendation["business_reasons"],
    "model_name": MODEL_NAME,
    "model_version": MODEL_VERSION,
    "prediction_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

        except Exception as e:

            logger.error(f"Prediction failed: {e}")

            raise PredictionError(
                f"Prediction failed.\n{e}"
            )