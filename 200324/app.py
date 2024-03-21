# app.py
from fastapi import FastAPI
import joblib

app = FastAPI()

# Load the trained model
model = joblib.load('model.pkl')

# Define endpoint for model prediction
@app.get("/predict/{input_data}")
async def predict(input_data: float):
    prediction = model.predict([[input_data]])
    return {"input": input_data, "prediction": prediction[0]}
