import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

# Loading the trained MobileNetV2 model
model = load_model('wheat_disease_classifier_v2.keras')

# CSS for styling the Streamlit app
st.markdown("""
    <style>
    .main {
        background-color: #f0f0f5;
        color: #2c3e50;
    }
    .title {
        color: #27ae60;
        font-size: 36px;
        text-align: center;
        font-weight: bold;
    }
    .upload-container {
        display: flex;
        justify-content: center;
        padding: 20px;
        margin-top: 50px;
    }
    .upload-button {
        background-color: #3498db;
        color: white;
        padding: 12px 30px;
        border-radius: 5px;
        font-size: 16px;
        cursor: pointer;
        border: none;
    }
    .upload-button:hover {
        background-color: #2980b9;
    }
    .prediction-container {
        margin-top: 30px;
        padding: 20px;
        background-color: #ffffff;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .prediction-title {
        font-size: 22px;
        font-weight: bold;
        color: #2c3e50;
    }
    .prediction-result {
        font-size: 18px;
        color: #27ae60;
    }
    .image-container {
        display: flex;
        justify-content: center;
        padding-top: 20px;
    }
    .footer {
        font-size: 14px;
        text-align: center;
        color: #7f8c8d;
        margin-top: 50px;
    }
    </style>
""", unsafe_allow_html=True)

# Title of the web app
st.markdown('<p class="title">Wheat Disease Classifier</p>', unsafe_allow_html=True)

# Description text
st.write("Upload an image of a wheat plant, and the model will classify it into one of the disease categories.")

# Image upload functionality
st.markdown('<div class="upload-container">', unsafe_allow_html=True)
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"], key="file_uploader", label_visibility="collapsed")
st.markdown('</div>', unsafe_allow_html=True)

# Function to preprocess the uploaded image
def preprocess_image(img):
    img = image.load_img(img, target_size=(224, 224))  # Resize the image to match model input
    img_array = image.img_to_array(img) / 255.0  # Normalize the image
    return np.expand_dims(img_array, axis=0)  # Add batch dimension

# If an image is uploaded, display it and make a prediction
if uploaded_file is not None:
    img = preprocess_image(uploaded_file)
    
    # Predict using the model
    prediction = model.predict(img)
    predicted_class = np.argmax(prediction, axis=1)

    # Map the predicted class to disease names
    class_names = ["Aphid", "Black Rust", "Blast", "Brown Rust", "Common Root Rot", 
                   "Fusarium Head Blight", "Healthy", "Leaf Blight", "Mildew", "Mite", 
                   "Septoria", "Smut", "Stem Fly", "Tan Spot", "Yellow Rust"]
    predicted_disease = class_names[predicted_class[0]]
    
    # Display uploaded image
    st.markdown('<div class="image-container">', unsafe_allow_html=True)
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Display prediction results
    st.markdown('<div class="prediction-container">', unsafe_allow_html=True)
    st.markdown(f'<p class="prediction-title">Prediction Result:</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="prediction-result">{predicted_disease}</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown('<p class="footer">Made with ❤️ by Brian Githinji | Wheat Disease Classification</p>', unsafe_allow_html=True)
