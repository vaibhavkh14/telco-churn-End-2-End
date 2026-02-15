import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from pathlib import Path


# Load trained model
BASE_DIR = Path(__file__).resolve().parent     # .../app
model = joblib.load(BASE_DIR.parent / "models" / "churn_pipeline.joblib")
app = FastAPI(title="Telco Churn Predictor")


class CustomerFeatures(BaseModel):
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float


@app.get("/")
def home():
    return {"message": "API is running"}


@app.post("/predict")
def predict(data: CustomerFeatures):
    df = pd.DataFrame([data.model_dump()])
    probability = model.predict_proba(df)[:, 1][0]
    prediction = int(probability >= 0.35)

    return {
        "churn_probability": round(float(probability), 4),
        "churn_prediction": prediction
    }
