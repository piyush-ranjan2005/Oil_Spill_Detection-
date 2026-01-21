OilWatch AI 🛢️
AI-Driven Oil Spill Identification and Monitoring System using Satellite Imagery and Deep Learning

Project Overview
OilWatch AI is an AI-driven system designed for the automatic detection and segmentation of oil spills in satellite imagery using deep learning techniques like CNN and U-Net. It provides environmental monitoring agencies with a fast, accurate, and automated solution to identify oil-contaminated regions, reducing reliance on slow and error-prone manual inspection methods.

Problem Statement
Oil spills are a critical environmental hazard, causing damage to marine ecosystems, affecting local economies, and requiring immediate response. Traditional monitoring methods rely on manual satellite image analysis, which is:
Time-consuming
Error-prone
Inefficient for large-scale monitoring

Solution: Develop an automated system that can detect oil spills and generate precise segmentation masks directly from satellite images, enabling near real-time monitoring and faster decision-making.

Solution Overview
OilWatch AI leverages satellite SAR imagery (Sentinel-1, PALSAR) and deep learning models (CNN, U-Net) to:
Automatically detect oil spills in satellite images
Produce pixel-level segmentation masks of contaminated regions
Visualize and highlight affected areas
Deploy a web interface for easy, real-time monitoring
This system can be accessed via a Streamlit or Flask interface, allowing environmental agencies to use it without technical expertise.

Deployment Link: OilWatch AI Web App
 (replace with actual link)

Key Features
Automatic detection of oil spills from satellite images
Pixel-level segmentation of oil-contaminated regions
Deep learning-based pattern recognition for high accuracy
Real-time visualization of affected areas
User-friendly web deployment for monitoring and analysis

Tech Stack
Component	Technology/Tool
Programming Language	Python
Deep Learning Models	CNN, U-Net
Satellite Data	Sentinel-1, PALSAR SAR imagery
Dataset	Refined Deep SAR Oil Spill (SOS) Dataset by Zenedo
Visualization & Deployment	Matplotlib, OpenCV, Streamlit, Flask
Image Processing	PIL, NumPy
Detailed Work Completed

The project was developed in 7 major stages:
Data Collection
Collected SAR satellite images (Sentinel-1, PALSAR)
Integrated the Refined Deep SAR Oil Spill (SOS) Dataset with pixel-level segmentation masks
Exploratory Data Analysis (EDA)
Visualized sample images and masks
Analyzed patterns in oil-contaminated regions
Checked dataset quality and class distribution
Data Preprocessing
Normalized and resized images for model compatibility
Augmented dataset using rotations, flips, and intensity adjustments
Prepared segmentation masks aligned with input images

Model Development
CNN: Extracted visual features and patterns of oil spills
U-Net: Built for pixel-level segmentation to accurately highlight affected regions

Training and Evaluation
Trained models using cross-entropy and Dice loss
Evaluated performance with metrics: IoU (Intersection over Union), Dice coefficient, accuracy, and loss curves
Tuned hyperparameters for optimal segmentation accuracy

Visualization of Results
Overlaid predicted segmentation masks on original satellite images
Generated clear, interpretable visuals for monitoring and reporting

Deployment
Developed a Streamlit web app for user-friendly interaction
Users can upload satellite images and receive real-time oil spill segmentation
Ensured smooth visualization and fast inference for practical use

Project Modules
Data Collection & EDA – Gathering and analyzing satellite data
Preprocessing – Normalization, augmentation, and mask preparation
Modeling – CNN & U-Net for detection and segmentation
Training & Evaluation – Model optimization and metric analysis
Visualization – Overlaying masks on images for clear interpretation
Deployment – Streamlit/Flask web interface for real-time usage

How to Run
Prerequisites:
Python 3.8+
Required libraries: tensorflow, opencv-python, Pillow, matplotlib, streamlit
Steps:
Clone the repository: git clone <repository-url>
cd OilWatch-AI
Install dependencies:
pip install -r requirements.txt
Run the web app (Streamlit example):
streamlit run app.py
Upload satellite images through the interface to detect oil spills and view segmentation masks.
Deployment Link: OilWatch AI Web App

Future Enhancements
Integrate real-time satellite feed for continuous monitoring
Add multi-spectral analysis to improve detection accuracy
Enable historical trend analysis for oil spill patterns
Develop a mobile version for on-field monitoring

Acknowledgements
This project is developed as part of the Infosys Springboard Internship program.
Dataset: Refined Deep SAR Oil Spill (SOS) Dataset by Zenedo

Inspired by research on oil spill detection using deep learning and SAR imagery
