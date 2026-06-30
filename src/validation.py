"""
Input validation for the Customer Churn Prediction Platform.
"""

import pandas as pd

from src.exceptions import ValidationError


def validate_input(data: pd.DataFrame) -> pd.DataFrame:
    """
    Validate input data before prediction.

    Parameters
    ----------
    data : pd.DataFrame
        Customer data for prediction.

    Returns
    -------
    pd.DataFrame
        Validated input data.

    Raises
    ------
    ValidationError
        If the input is invalid.
    """

    # Check input type
    if not isinstance(data, pd.DataFrame):
        raise ValidationError("Input must be a pandas DataFrame.")

    # Check empty DataFrame
    if data.empty:
        raise ValidationError("Input data is empty.")

    return data