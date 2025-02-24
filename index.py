import gradio as gr
import tensorflow as tf
import numpy as np
from PIL import Image

# Load the trained model
model = tf.keras.models.load_model(r"./fruits_classification.keras")  # Update with your model path

# Define class labels (Update with your actual class names)
class_labels = ["Apple", "Banana", "Orange", "Strawberry", "Grapes"]

# Function to preprocess the uploaded image
def predict_image(image_path):
    img = tf.keras.preprocessing.image.load_img(image_path, target_size=(100, 100))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Rescale
    
    prediction = model.predict(img_array)
    predicted_class = class_names[np.argmax(prediction)]
    confidence = np.max(prediction)
    
    return predicted_class, confidence
# Gradio interface
iface = gr.Interface(
    fn=predict_image,
    inputs=gr.Image(type="pil"),
    outputs=gr.Label(num_top_classes=1),
    title="🍎🍌 Fruit Classifier 🍊🍓",
    description="Upload an image of a fruit, and the model will predict its category!"
)

# Launch the Gradio app
iface.launch()