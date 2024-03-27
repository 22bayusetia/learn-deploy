import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from fastapi import FastAPI
from pydantic import BaseModel

# Load the Boston Housing dataset from the original source
data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.2, random_state=42)

# Initialize and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Define the FastAPI application
app = FastAPI()

# Define input data schema
class InputData(BaseModel):
    CRIM: float
    ZN: float
    INDUS: float
    CHAS: float
    NOX: float
    RM: float
    AGE: float
    DIS: float
    RAD: float
    TAX: float
    PTRATIO: float
    B: float
    LSTAT: float

# Define prediction endpoint
@app.post("/predict/")
async def predict(data: InputData):
    input_data = np.array([[data.CRIM, data.ZN, data.INDUS, data.CHAS, data.NOX, 
                            data.RM, data.AGE, data.DIS, data.RAD, data.TAX, 
                            data.PTRATIO, data.B, data.LSTAT]])
    prediction = model.predict(input_data)
    return {"prediction": prediction[0]}

# Define a root endpoint for basic information
@app.get("/")
async def root():
    return {"message": "Welcome to the Boston Housing Price Prediction API!"}

# Optional: Run the FastAPI application locally
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
