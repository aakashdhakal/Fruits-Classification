# 🍎 Fruit Classification with Deep Learning

## 📌 Project Overview
This project is a deep learning-based fruit classification system that utilizes a convolutional neural network (CNN) trained on the **Fruits-360** dataset. The model is capable of predicting fruit types from both images and a real-time webcam feed.

## 🚀 Features
- **Train a CNN model** to classify different fruit types.
- **Predict fruit from images** using the trained model.
- **Real-time fruit classification using a webcam**.
- **Web API support** to integrate predictions into web applications.

## 🏗️ Technologies Used
- **Python** (TensorFlow, OpenCV, NumPy, Matplotlib, Flask)
- **TensorFlow/Keras** for deep learning
- **OpenCV** for real-time webcam processing
- **Flask** for web API

## 📂 Project Structure
```
📁 fruit-classification
│-- 📂 fruits             # Training and testing dataset
     |-- 📂 train         # Training Dataset
     |-- 📂 test          # Testing Dataset
│-- 📂 website            # Files for Flask Website
     |-- 📂 static        # Web static files (if applicable)
     |-- 📂 templetes     # Web templates (if applicable)
     |-- 📜 app.py        # Flask API for fruit classification
│-- 📜 model.ipynb        # Jupyter notebook for training the CNN model
│-- 📜 requirements.txt   # Required dependencies
│-- 📜 README.md          # Project documentation
```

## 🎯 How to Use
### 1️⃣ Setup Environment
```sh
pip install -r requirements.txt
```

### 2️⃣ Train the Model
Run `model.ipynb` to train the CNN model and save it.

### 3️⃣ Predict from Image
Run `app.py` and send an image for prediction:
```sh
python app.py
```

## 📌 Example Prediction Output
```json
{
  "predicted_fruit": "Apple",
  "confidence_level": 98.7
}
```

## 🤖 Future Improvements
- Increase dataset size for better accuracy.
- Improve real-time detection speed.

## 📜 License
This project is open-source and available under the **MIT License**.
