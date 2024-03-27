from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import io

app = Flask(__name__)

# Load the trained model
model = load_model('handwritten_trained.h5')

@app.route('/')
def index():
    return "Welcome to the Handwritten Digit Recognition API. Send a POST request to /predict with an image of a handwritten digit to get a prediction."

@app.route('/predict', methods=['POST'])
def predict_digit():
    # Get image data from the request
    image_data = request.files['image'].read()
    image = Image.open(io.BytesIO(image_data))
    
    # Preprocess the image
    image = image.resize((28, 28))
    image = image.convert('L')  # Convert to grayscale
    image = np.array(image) / 255.0  # Normalize pixel values

    # Use the trained model to predict the digit
    prediction = model.predict(image.reshape(1, 28, 28, 1))
    predicted_digit = np.argmax(prediction)

    # Return the predicted digit as JSON
    return jsonify({'predicted_digit': int(predicted_digit)})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
