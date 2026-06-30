"""
Logging configuration for the Customer Churn Prediction Platform.
"""

import logging
from pathlib import Path

from src.config import LOGS_DIR, PREDICTION_LOG

# Create logs folder if it doesn't exist
Path(LOGS_DIR).mkdir(parents=True, exist_ok=True)

# Configure logging
logging.basicConfig(
    filename=PREDICTION_LOG,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Logger object
logger = logging.getLogger(__name__)