from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import numpy as np
import logging

# Create FastAPI app
app = FastAPI()

# Load the trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Define request body schema
class InputData(BaseModel):
    data: list

# Configure logging
logging.basicConfig(level=logging.ERROR)

@app.get("/")
async def root():
    return {"message": "Welcome to the Regression API!"}

# Define prediction endpoint
@app.post("/predict")
async def predict(data: InputData):
    input_features = data.data
    if len(input_features) != 4:
        raise HTTPException(status_code=400, detail="Input should contain 4 features.")
    try:
        input_features = [float(feature) for feature in input_features]
    except ValueError:
        raise HTTPException(status_code=400, detail="Input features must be numeric.")
    input_array = np.array(input_features).reshape(1, -1)
    prediction = model.predict(input_array)[0]
    return {"prediction": prediction.item()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8081)

