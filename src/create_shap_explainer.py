import joblib
import shap

# Load the trained model
model = joblib.load(r"C:\\Users\\Hey!\\OneDrive\\Desktop\\Customer churn prediction & retention Platform\\models\\best_model.pkl")

# Create SHAP TreeExplainer
explainer = shap.TreeExplainer(model)

# Save the explainer
joblib.dump(explainer, r"C:\\Users\\Hey!\\OneDrive\\Desktop\\Customer churn prediction & retention Platform\\models\\shap_explainer.pkl")

print("✅ SHAP Explainer created successfully!")