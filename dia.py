from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI()

# Load trained model
model = joblib.load("diabetes.pkl")

class Customer(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int

@app.get("/")
def home():
    return {"message": "Welcome to Diabetes Prediction API"}

@app.post("/predict")
def predict(data: Customer):

    df = pd.DataFrame([data.model_dump()])

    prediction = model.predict(df)

    result = "Diabetic" if prediction[0] == 1 else "Not Diabetic"

    return {
        "prediction": result
    }