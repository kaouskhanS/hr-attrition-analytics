from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

model = joblib.load("../model/attrition_model.pkl")

@app.get("/")
def home():
    return {"message": "HR Attrition API Running"}

@app.post("/predict")
def predict(data: dict):
    values = np.array([list(data.values())])
    pred = model.predict(values)[0]
    return {"attrition_risk": int(pred)}
