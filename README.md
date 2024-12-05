
# **Wheat Disease and Pest Diagnosis Model**
![8dac43b028d2a68f1c2439ad0b7a75b0](https://github.com/user-attachments/assets/d59f5042-6978-4ca4-b9bb-7336abf03555)![d4de8a94d7387983c884475f0c1cfc61](https://github.com/user-attachments/assets/127cbcbb-a1f0-45bd-b0a4-bee56eb10d2b)



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
#### Exploratory Data Analysis (EDA) Findings

## 1. Overview
The dataset consists of wheat plant disease images divided into three subsets: training, validation, and test. There are 15 classes, each representing a specific wheat disease or pest.

---

## 2. Class Distribution

### Training Set
- **Most Represented Classes**:
  - Yellow Rust: 1,301 images
  - Brown Rust: 1,167 images
- **Least Represented Classes**:
  - Stem Fly: 172 images
  - Septoria: 349 images

This significant class imbalance may affect model performance, requiring techniques like oversampling or data augmentation for underrepresented classes.

---

## 3. Image Dimensions

- **Common Dimensions**: Most images have a resolution of `(224, 224)` pixels.
- **Inconsistencies**:
  - Some classes have images with significantly different resolutions, which might require resizing for uniformity.

### Visualization: Distribution of Image Dimensions
- Width and height distributions indicate minor variations, suggesting the need for normalization before model training.

---

## 4. Dataset Splits

- **Class Imbalance Across Splits**:
  - The training set has sufficient data for most classes but needs balancing.
  - Validation and test sets are not evenly distributed, affecting model evaluation reliability.

---

## 5. Recommended Actions

1. **Class Imbalance**:
   - Apply data augmentation or oversampling for underrepresented classes (`Stem Fly`, `Septoria`, etc.).
2. **Resize Images**:
   - Standardize image dimensions to `(224, 224)` to ensure uniformity.
3. **Augment Validation/Test Data**:
   - Use training images to supplement validation and test sets, ensuring all classes are represented.

---

## 6. Visualizations

### Class Distribution in Training Set
The bar chart below illustrates the class distribution in the training set, highlighting the imbalance across classes:

- **Most Represented Classes**: Yellow Rust, Brown Rust.
- **Least Represented Classes**: Stem Fly, Septoria.
![image](https://github.com/user-attachments/assets/02f5aed5-ed7f-490d-bbe5-a789a0dcba39)



### Image Dimensions
The histograms below show the distribution of image dimensions (width and height), indicating minor variations:

- **Peak Dimensions**: `(224, 224)`.
- **Outliers**: A few classes have significantly larger or smaller images.
![image](https://github.com/user-attachments/assets/a32036ff-80f1-4384-be50-2fa4b2c004c7)

---

## Conclusion

The dataset is well-suited for training machine learning models but requires preprocessing to address:
1. **Class imbalance**: Augment minority classes.
2. **Validation/Test augmentation**: Ensure sufficient representation across splits.
3. **Image resizing**: Standardize dimensions for consistent model input.


### **2. Preprocessing**
- Resized all images to 224x224.
- Normalized pixel values.
- Augmented data to address class imbalances.

### **3. Model Development**
- Transfer Learning using `MobileNetV2`.
- Optimized hyperparameters for improved performance.
- Metrics:
  - Accuracy: **71.3%**
  - Precision: **72**
  - Recall: **70%**

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
