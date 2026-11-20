from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI(title="Diabetes Regression API")

# Load the saved dictionary
model_data = joblib.load("diabetes.pkl")

model = model_data["model"]

print("Model type:", type(model))
print("Model loaded successfully")


@app.get("/")
def home():
    return {
        "message": "Diabetes Regression API is running"
    }


@app.post("/predict")
def predict(data: dict):

    # Convert JSON to DataFrame
    input_df = pd.DataFrame([data])

    # Predict
    prediction = model.predict(input_df)

    return {
        "prediction": float(prediction[0])
    }