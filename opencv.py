# Use webcam to predict in real-time
import cv2
import numpy as np
import tensorflow as tf
import os


model = tf.keras.models.load_model('./fruits_classification.keras')

# Define class labels
class_labels =  os.listdir('./fruits/train')

# Define the predict_image function
def predict_image(image_path, model, class_labels):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (100, 100))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    predictions = model.predict(img)
    predicted_class = class_labels[np.argmax(predictions)]
    confidence = np.max(predictions)
    return predicted_class, confidence

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        continue
    
    # Save the frame as an image
    cv2.imwrite('webcam.jpg', frame)
    
    # Predict the class of the saved image
    predicted_class, confidence = predict_image('webcam.jpg', model, class_labels)
    
    # Write the predicted class and confidence on the frame
    cv2.putText(frame, f"Class: {predicted_class}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, f"Confidence: {confidence:.2f}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    
    # Display the frame
    cv2.imshow("Webcam", frame)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()