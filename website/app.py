import flask
from flask import request, jsonify, render_template
import tensorflow as tf
import numpy as np
import os
import random

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Load the model
model = tf.keras.models.load_model('./fruits_classification.keras')

# Define the image size
IMAGE_SIZE, IMAGE_SIZE = 100, 100

# Function to predict image
def predict_image(img_path):
    img = tf.keras.preprocessing.image.load_img(img_path, target_size=(IMAGE_SIZE, IMAGE_SIZE))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Rescale
    
    prediction = model.predict(img_array)
    predicted_index = np.argmax(prediction)
    confidence = np.max(prediction)
    return predicted_index, confidence

def class_names():
    # Extract class names from the folder names
    fruits_names = ['apple','avocado','banana','blueberry','cherry','dragonfruit','grape','guava','kiwi','lychee','mango','orange','papaya','pear','pineapple','pomegranate','raspberry','strawberry','watermelon']
    return fruits_names

@app.route('/', methods=['GET'])
def index():
    return render_template('form.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'fruit' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['fruit']
    randomNumber = random.randint(0, 100000)
    file_path = f'predict_fruit/fruit-{randomNumber}.jpg'
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    file.save(file_path)
    # Predict the fruit
    predicted_index, confidence_level = predict_image(file_path)
    fruit_names = class_names()  # Update with your actual class names
    predicted_fruit = fruit_names[predicted_index]
    #convert predicted class to string
    return jsonify({'predicted_fruit': predicted_fruit, 'confidence_level': float(confidence_level)})

if __name__ == '__main__':
    app.run()