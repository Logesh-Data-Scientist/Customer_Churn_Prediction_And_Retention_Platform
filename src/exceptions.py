"""
Custom exceptions for the Customer Churn Prediction Platform.
"""


class PredictionError(Exception):
    """
    Raised when an error occurs during model prediction.
    """

    pass


class ValidationError(Exception):
    """
    Raised when input data validation fails.
    """

    pass