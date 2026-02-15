
# 🚀 Telco Customer Churn Prediction (End-to-End ML Deployment)

An end-to-end Machine Learning project that predicts customer churn probability using a production-ready pipeline, exposed via FastAPI and deployed on AWS Elastic Beanstalk using Docker.

---

## 🌐 Live Deployment (AWS)

🔗 Base URL  
http://telco-churn-env.eba-pjwm3b75.eu-north-1.elasticbeanstalk.com/

📘 Swagger API Docs  
http://telco-churn-env.eba-pjwm3b75.eu-north-1.elasticbeanstalk.com/docs

---

## 📌 Problem Statement

Telecom companies face high customer churn. This project builds a machine learning model to predict the probability of a customer leaving the service based on demographic and service-related features.

---

## 🧠 Machine Learning Pipeline

- Data Cleaning & Feature Engineering
- Handling Categorical Variables using Pipeline
- Model Training (scikit-learn)
- Probability Threshold Tuning (0.35)
- Model Serialization using joblib

The entire preprocessing + model is bundled inside a single scikit-learn Pipeline for production safety.

---

## 🔌 API Endpoints

### `GET /`
Returns API health status.

### `POST /predict`
Predicts churn probability and churn label.

---

## 📥 Sample Request

```json
{
  "gender": "Male",
  "SeniorCitizen": 0,
  "Partner": "Yes",
  "Dependents": "No",
  "tenure": 12,
  "PhoneService": "Yes",
  "MultipleLines": "No",
  "InternetService": "Fiber optic",
  "OnlineSecurity": "No",
  "OnlineBackup": "Yes",
  "DeviceProtection": "No",
  "TechSupport": "No",
  "StreamingTV": "Yes",
  "StreamingMovies": "No",
  "Contract": "Month-to-month",
  "PaperlessBilling": "Yes",
  "PaymentMethod": "Electronic check",
  "MonthlyCharges": 85.5,
  "TotalCharges": 1026.0
}

📤 Sample Response
{
  "churn_probability": 0.4776,
  "churn_prediction": 1
}


churn_probability → Probability of churn

churn_prediction → 1 = Likely to churn, 0 = Not likely

🏗️ Project Architecture
User Request
     ↓
AWS Elastic Beanstalk
     ↓
Docker Container
     ↓
FastAPI
     ↓
scikit-learn Pipeline
     ↓
Prediction Response

🛠️ Tech Stack

Python

FastAPI

scikit-learn

Pandas, NumPy

Docker

AWS Elastic Beanstalk

IAM & ECR (container workflow)

🖥️ Run Locally
Install dependencies
pip install -r requirements.txt

Start API
python -m uvicorn app.main:app --reload


Visit:

http://127.0.0.1:8000/docs

🐳 Run with Docker
docker build -t churn-api .
docker run -p 8000:8000 churn-api

📈 Resume Highlight

Telco Customer Churn Prediction (AWS Deployed)
Built and deployed an end-to-end ML system using a scikit-learn Pipeline, exposed via FastAPI, containerized with Docker, and deployed to AWS Elastic Beanstalk with a live public inference endpoint.

⚠️ Note on Cloud Cost

Elastic Beanstalk provisions an EC2 instance.
Terminate the environment after demo to avoid billing.

👨‍💻 Author

Vaibhav Khandelwal
End-to-End Machine Learning & Deployment Project