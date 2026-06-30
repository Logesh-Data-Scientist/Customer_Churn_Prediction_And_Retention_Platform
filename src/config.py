from pathlib import Path

# ===========================
# PROJECT ROOT DIRECTORY
# ===========================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# ===========================
# FOLDERS
# ===========================

MODELS_DIR = PROJECT_ROOT / "models"
PROCESSED_DATA_DIR = PROJECT_ROOT / "processed_data"
ARTIFACTS_DIR = PROJECT_ROOT / "artifacts"
LOGS_DIR = PROJECT_ROOT / "logs"
CONFIGS_DIR = PROJECT_ROOT / "configs"

# ===========================
# MODEL FILES
# ===========================

BEST_MODEL_PATH = MODELS_DIR / "best_model.pkl"
FEATURE_COLUMNS_PATH = MODELS_DIR / "feature_columns.pkl"

# ===========================
# MODEL INFORMATION
# ===========================

MODEL_NAME = "Random Forest"
MODEL_VERSION = "1.0.0"

# ===========================
# LOG FILES
# ===========================

PREDICTION_LOG = LOGS_DIR / "prediction.log"
TRAINING_LOG = LOGS_DIR / "training.log"