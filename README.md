

🛢️AI-Driven System for Oil Spill Identification and Monitoring

📌 Project Overview

This project focuses on detecting and segmenting oil spill regions from satellite images using deep learning–based image segmentation.
The goal is to assist in environmental monitoring by automatically identifying oil spill areas accurately and efficiently.

🎯 Objectives

Detect oil spill regions from satellite imagery

Perform pixel-level segmentation using deep learning

Handle class imbalance between oil and non-oil regions

Deploy the trained model as a user-friendly web application

🗂️ Dataset

Satellite images with corresponding binary masks

Mask values:

0 → Non-oil region

1 → Oil spill region

The dataset is divided into:

Training set

Validation set

🔍 Data Exploration & Preprocessing

The following steps were performed:

Dataset structure verification

Visualization of images and masks (sanity check)

Image size analysis

Oil vs non-oil class distribution analysis

Oil spill area coverage analysis

Data augmentation using Albumentations

Resizing

Horizontal & vertical flips

Conversion to PyTorch tensors

🧠 Model Architecture

Model: U-Net

Encoder: ResNet-34 (ImageNet pretrained)

Framework: PyTorch & segmentation-models-pytorch

Input: RGB satellite images

Output: Binary segmentation mask

⚙️ Training Details

Loss Function:

Dice Loss + Binary Cross-Entropy Loss (to handle class imbalance)

Optimizer: Adam

Learning Rate: 1e-4

Device: GPU (if available)

Training loss showed a consistent decrease across epochs, indicating effective learning.

📊 Evaluation
Quantitative Evaluation

Dice Score

Intersection over Union (IoU)

Qualitative Evaluation

Visualization of predicted masks vs ground truth

Comparison between oil and non-oil images

🌐 Deployment

The trained model has been successfully deployed using Streamlit.

🔗 Live Application:
👉 https://oil-spill-detection-0820.streamlit.app/

Features:

Upload a satellite image

Automatically generate oil spill segmentation output

Visual comparison of input image and predicted mask

🛠️ Technologies Used

Python

PyTorch

OpenCV

Albumentations

NumPy

Matplotlib

Streamlit


🚀 Future Improvements

Improve model generalization with more data
Add multi-class segmentation
Optimize model size for faster inference
Enhance UI with confidence visualization

👩‍💻 Author

Kajal Jain
B.Tech Computer Science
AI / Machine Learning Internship Project


