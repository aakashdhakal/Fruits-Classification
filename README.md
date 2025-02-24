🍎 Fruit Classification using Deep Learning

🎯 Project Overview

This project is a real-time fruit classification system that uses a deep learning model to identify different types of fruits from webcam images. Built with TensorFlow and OpenCV, this project provides a fast and accurate way to recognize fruits using a custom-trained Convolutional Neural Network (CNN).

🛠️ Tech Stack

Python (Primary Language)

TensorFlow/Keras (Model Training & Prediction)

OpenCV (Webcam Image Capture & Preprocessing)

NumPy & Pandas (Data Handling)

Matplotlib (Data Visualization)

Flask (Optional) (For API Deployment)

📂 Project Structure

📁 Fruit-Classification
├── 📂 dataset          # Training & testing dataset
├── 📂 models           # Saved trained models
├── 📂 scripts          # Helper scripts for training & prediction
├── model.ipynb         # Jupyter Notebook for training the model
├── Opencv.ipynb        # Jupyter Notebook for real-time prediction
├── app.py              # Flask API (if applicable)
├── requirements.txt    # Dependencies list
└── README.md           # Project documentation

🚀 Features

✅ Train a deep learning model to classify fruits with high accuracy. ✅ Capture images from the webcam and predict the fruit type in real time. ✅ Efficient preprocessing using OpenCV. ✅ Lightweight and optimized for deployment.

🎥 Real-Time Prediction

Run the following command to start the real-time fruit classification:

python real_time_fruit_classification.py

📦 Installation

Clone the repository:

git clone https://github.com/yourusername/fruit-classification.git
cd fruit-classification

Install dependencies:

pip install -r requirements.txt

Run the Jupyter notebooks for training and testing.

Execute the script to start real-time classification.

📊 Model Performance

The model was trained on the Fruits-360 dataset and additional images, achieving an accuracy of 90%+ on the test set.

🤖 Future Improvements

🔹 Improve model accuracy with data augmentation. 🔹 Implement a mobile-friendly version. 🔹 Enhance the UI for better user experience.

📝 License

This project is open-source and available under the MIT License.

🚀 Made with passion by Aakash Dhakal ✨
