from pathlib import Path

from flask import Flask, render_template, request

from utils.prediction import predict_customer

PROJECT_ROOT = Path(__file__).resolve().parent
app = Flask(
    __name__,
    template_folder=str(PROJECT_ROOT / "web app"),
    static_folder=str(PROJECT_ROOT / "web app"),
)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    result = predict_customer(request.form)

    return render_template(
        "result.html",
        prediction=result["prediction"],
        probability=result["probability"],
        risk=result["risk"],
        recommendation=result["recommendation"]
    )


if __name__ == "__main__":
    app.run(debug=True)