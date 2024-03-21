# model.py
from sklearn.linear_model import LinearRegression
import joblib

try:
    # Create and train the model
    model = LinearRegression()
    X_train = [[1], [2], [3], [4], [5]]
    y_train = [2, 4, 5, 4, 5]
    model.fit(X_train, y_train)

    # Save the trained model
    joblib.dump(model, 'model.pkl')
    print("Model trained and saved successfully!")
except Exception as e:
    print("An error occurred:", e)
