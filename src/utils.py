"""
Utility functions for the Customer Churn Prediction Platform.
"""

import json
import joblib
from pathlib import Path


def save_pickle(obj, file_path):
    """
    Save any Python object as a pickle file.

    Parameters:
        obj : Python object
        file_path : Path where the object will be saved
    """
    file_path = Path(file_path)
    file_path.parent.mkdir(parents=True, exist_ok=True)

    joblib.dump(obj, file_path)


def load_pickle(file_path):
    """
    Load a pickle file.

    Parameters:
        file_path : Path to pickle file

    Returns:
        Loaded Python object
    """
    return joblib.load(file_path)


def save_json(data, file_path):
    """
    Save a dictionary as a JSON file.
    """
    file_path = Path(file_path)
    file_path.parent.mkdir(parents=True, exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def load_json(file_path):
    """
    Load a JSON file.

    Returns:
        Dictionary
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)