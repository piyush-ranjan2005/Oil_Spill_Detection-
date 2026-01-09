🛢️ Oil Spill Detection Using Deep Learning
📌 Project Overview

Oil spills in oceans cause serious environmental damage and threaten marine life. Manual monitoring is slow and inefficient.
This project uses Deep Learning and Satellite Images to automatically detect oil spills from ocean surface images.

The system classifies satellite images into:

Oil Spill

Non-Oil Spill

🎯 Project Objectives

Detect oil spills accurately using satellite images

Reduce manual monitoring efforts

Improve early detection for environmental protection

Build an end-to-end AI solution from data to deployment

🧠 Problem Statement

Traditional oil spill detection methods are time-consuming and error-prone.
There is a need for an automated, intelligent system that can analyze satellite images and identify oil spills with high accuracy.

🧪 Dataset Description

Source: Satellite imagery dataset

Classes:

Oil Spill

Non Oil Spill

Data Type: Image data (JPEG / PNG)

Task Type: Binary Image Classification

📁 Dataset Folder Structure
dataset/
│
├── Oil_Spill/
│   ├── image1.jpg
│   ├── image2.jpg
│
├── Non_Oil_Spill/
│   ├── image1.jpg
│   ├── image2.jpg

🔍 Project Workflow
Data Collection
      ↓
EDA (Exploratory Data Analysis)
      ↓
Data Preprocessing
      ↓
Model Building
      ↓
Model Training
      ↓
Model Evaluation
      ↓
Model Saving
      ↓
Deployment

📊 Exploratory Data Analysis (EDA)

EDA helps understand the dataset before training the model.

EDA Steps:

Dataset size analysis

Class distribution check

Sample image visualization

Image resolution analysis

Detecting class imbalance

📌 Notebook:

EDA_and_preprocessing_oil_spill 9.ipynb

🧹 Data Preprocessing

Preprocessing prepares data for model training.

Steps:

Image loading from folders

Resizing images to fixed dimensions

Normalizing pixel values (0–255 → 0–1)

Encoding class labels

Train-test data split

Optional data augmentation

🤖 Model Architecture

Model Type: Convolutional Neural Network (CNN)

Framework: TensorFlow / Keras

Layers Used:

Convolution Layers

MaxPooling Layers

Flatten Layer

Dense Layers

Output Layer (Sigmoid)

🏋️ Model Training

Loss Function: Binary Cross-Entropy

Optimizer: Adam

Evaluation Metric: Accuracy

Epochs: As required

Batch Size: Optimized during training

📈 Model Evaluation

The trained model is evaluated using:

Accuracy

Training vs Validation loss

Training vs Validation accuracy

📊 Final Accuracy
Model Accuracy: ~82%


This accuracy is acceptable for academic and prototype-level deployment.

💾 Model Saving

The trained model is saved for future use.

model.save("oil_spill_model.keras")

🌐 Deployment

The trained model can be deployed using:

Streamlit Web App

Flask API

Cloud Platforms (optional)

Deployment Features:

Upload satellite image

Predict Oil Spill / Non-Oil Spill

Display prediction result instantly

🛠️ Tools & Technologies Used

Programming Language: Python

IDE: Google Colab / Jupyter Notebook

Libraries:

NumPy

Pandas

Matplotlib

Seaborn

OpenCV / PIL

Scikit-learn

TensorFlow / Keras

Deployment: Streamlit / Flask

📂 Project Structure
Oil-Spill-Detection/
│
├── dataset/
├── EDA_and_preprocessing_oil_spill 9.ipynb
├── model_training.ipynb
├── oil_spill_model.keras
├── app.py
├── requirements.txt
└── README.md

✅ Advantages of the System

Fast and automated detection

Reduces human effort

Scalable and reusable

Can be integrated with satellite monitoring systems

⚠️ Limitations

Depends on image quality

Needs larger datasets for higher accuracy

Environmental factors may affect prediction

🔮 Future Enhancements

Use transfer learning (ResNet, VGG, EfficientNet)

Improve accuracy with larger datasets

Real-time satellite data integration

Mobile application development

👩‍💻 Author

Kalyani Patil
B.Tech – Artificial Intelligence
Academic Project

📌 Conclusion

This project successfully demonstrates how Deep Learning can be used to detect oil spills from satellite images.
It provides a complete AI pipeline from EDA to Deployment, making it suitable for real-world applications and academic evaluation.
