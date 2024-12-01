
# **Wheat Disease and Pest Diagnosis Model**
![8dac43b028d2a68f1c2439ad0b7a75b0](https://github.com/user-attachments/assets/d59f5042-6978-4ca4-b9bb-7336abf03555)!![d4de8a94d7387983c884475f0c1cfc61](https://github.com/user-attachments/assets/127cbcbb-a1f0-45bd-b0a4-bee56eb10d2b)



> An image classification model to diagnose wheat crop pests and diseases, deployed on a web platform to assist smallholder farmers in improving crop yield.

---

## **Overview**
Smallholder farmers face challenges in detecting and managing wheat pests and diseases, leading to reduced yields. This project develops a diagnostic tool leveraging machine learning to classify wheat crop images into healthy and diseased categories, providing actionable insights for timely intervention.

### **Key Features**
- Diagnose wheat crop pests and diseases from images.
- Confidence scores for predictions.
- User-friendly web app for image uploads and results.

---

## **Business Need**
The tool is designed to empower farmers by:
- Enabling early detection and treatment of wheat crop issues.
- Reducing the risk of yield loss.
- Increasing efficiency in managing crop health.

---

## **Dataset**
- **Source**: [Wheat Plant Diseases Dataset](https://www.kaggle.com/datasets/kushagra3204/wheat-plant-diseases)
- **Classes**:
  - **Pests**: (e.g., Wheat Aphids)
  - **Diseases**: Leaf Rust, Stem Rust, Yellow Rust, etc.
  - **Healthy**: Wheat without any visible issues.

---

## **Project Workflow**
### **1. Data Analysis**
- Exploratory Data Analysis (EDA) to understand class distributions and identify data quality issues.

### **2. Preprocessing**
- Resized all images to 224x224.
- Normalized pixel values.
- Augmented data to address class imbalances.

### **3. Model Development**
- Transfer Learning using `ResNet50`.
- Optimized hyperparameters for improved performance.
- Metrics:
  - Accuracy: **xx%**
  - Precision: **xx%**
  - Recall: **xx%**

### **4. Deployment**
- Deployed a user-friendly Streamlit app.
- Features:
  - Image upload button.
  - Prediction results with confidence scores.

---

## **Installation**
### **Prerequisites**
- Python 3.8+
- Libraries: TensorFlow, Keras, Streamlit, NumPy, Pandas, OpenCV.

### **Setup**
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/wheat-disease-diagnosis.git
