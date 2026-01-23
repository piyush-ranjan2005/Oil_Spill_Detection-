🛢️ AI-Driven Oil Spill Detection Using Satellite SAR Imagery

“Automated environmental monitoring using deep learning & remote sensing”

Built with Python | Powered by Deep Learning | Visualized with Streamlit
License: Academic / Internship Project

📖 Table of Contents

1 Project Overview
2 Why This Project Exists
3 Key Features
4 System Architecture
5 Tech Stack
6 Dataset Description
7 Repository Structure
8 Notebook Overview
9 Module-Wise Implementation
10 Results & Visualizations
11 Deployment (Status & Details)
12 How to Run the Project
13 Screenshots
14 Key Learnings
15 Project Goals
16 Contributor Details
17 Acknowledgments
18 Final Notes

🤔 Project Overview

Oil spills are among the most devastating environmental disasters, causing long-term damage to marine ecosystems, coastal biodiversity, and economic activities.

This project presents an AI-based oil spill detection system that uses Synthetic Aperture Radar (SAR) satellite imagery and deep learning-based image segmentation to automatically identify oil spill regions from satellite images.

Unlike traditional manual monitoring methods, this system provides:

Faster detection

Objective analysis

Scalable monitoring capability

💡 Why This Project Exists

Real-world oil spill monitoring faces several challenges:

Manual inspection of satellite images is slow and error-prone

Optical images are affected by clouds and lighting

Look-alike phenomena (low wind areas) confuse traditional algorithms

Early detection is critical but difficult

This project addresses these issues by combining:

SAR satellite data

Deep learning segmentation models

Robust preprocessing and evaluation techniques

✨ Key Features

🔍 Automated Oil Spill Detection
Detects oil spill regions directly from satellite SAR images.

🧠 Deep Learning Segmentation Model
Uses a U-Net architecture optimized for pixel-level classification.

🖼️ Clear Visual Outputs
Displays:

Original satellite image

Ground truth mask

Predicted segmentation mask

Overlay visualization

📊 Quantitative Evaluation
Evaluates model performance using:

Dice Coefficient

IoU (Intersection over Union)

Accuracy, Precision, Recall

🌐 Deployment-Ready Design
Streamlit-based UI developed to allow interactive testing.

🏗️ System Architecture

High-Level Workflow

Satellite SAR image input

Image preprocessing & normalization

Deep learning model inference

Segmentation mask prediction

Visualization & analysis

🛠️ Tech Stack
Layer	Technology	Purpose / Usage
Programming Language	Python	Core implementation of the complete pipeline
Deep Learning Framework	TensorFlow, Keras	Model development, training, and inference
Model Architecture	U-Net (CNN-based)	Oil spill segmentation from SAR images
Image Processing	NumPy, PIL	SAR image loading, preprocessing, resizing
Data Handling	NumPy, Pandas	Dataset manipulation and numerical operations
Visualization	Matplotlib	Visualizing masks, overlays, and results
Satellite Data Type	Sentinel-1 SAR	Input satellite imagery for oil spill detection
Evaluation Metrics	Dice Coefficient, IoU, Accuracy, Precision, Recall	Model performance evaluation
Deployment (Optional)	Streamlit	Web-based interface for real-time inference
Environment	Google Colab / Local Machine	Model training and experimentation
Version Control	Git & GitHub	Source code management and collaboration

🗂️ Dataset Description
Attribute	Details
Dataset Source	Zenodo (Oil Spill Detection Dataset)
Satellite Type	Sentinel-1 SAR
Image Format	Grayscale SAR Images
Annotation	Binary Segmentation Masks
Classes	Oil Spill, Background
Final Resolution	256 × 256

Why SAR Data?

Works in all weather conditions

Effective for detecting surface roughness differences

Suitable for maritime monitoring

📂 Repository Structure
Oil_Spill_Detection/
│
├── notebooks/
│   └── Oil_Spill_Detection_End_to_End.ipynb
│
├── models/
│   └── unet_oil_spill_model.h5
│
├── screenshots/
│   ├── sample_input_image.png
│   ├── predicted_mask.png
│   └── overlay_visualization.png
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore

📓 Notebook Overview
Notebook	Description
Oil_Spill_Detection_End_to_End.ipynb	Complete implementation of Modules 2–5

This notebook includes:

Data exploration

Preprocessing

Model development

Training & evaluation

Visualization of results

🧱 Module-Wise Implementation
✅ Module 1: Data Collection

Acquired Sentinel-1 SAR satellite images

Obtained labeled oil spill segmentation masks

Organized dataset into structured directories

Verified image-mask alignment

✅ Module 2: Data Exploration & Preprocessing

Exploration

Visualized SAR images and masks

Analyzed pixel intensity distributions

Studied oil vs non-oil regions

Preprocessing Steps

Step	Description
Resizing	Standardized to 256 × 256
Normalization	Pixel values scaled to [0,1]
Channel Handling	Single-channel SAR images
Augmentation	Flip, rotate, normalize
✅ Module 3: Model Development (Segmentation)

Implemented U-Net architecture

Encoder-decoder with skip connections

Designed for binary segmentation

Optimized for SAR image input

✅ Module 4: Training & Evaluation

Training

Loss Functions: Dice Loss + Binary Cross-Entropy

Optimizer: Adam

Validation-based tuning

Evaluation Metrics

Dice Coefficient

IoU

Accuracy

Precision & Recall

✅ Module 5: Visualization of Results

Side-by-side comparison of:

Original SAR image

Ground truth mask

Predicted mask

Overlay visualization for clear interpretation


📊 Results & Screenshots

Screenshots demonstrating model performance are available in the screenshots/ directory.

Output	        Description
Input Image	    Raw SAR satellite image
Prediction	    Model-generated segmentation
Overlay	        SAR image + predicted mask

🚀 Module 6: Deployment (Status)
⚠️ Status: Attempted & Documented

A Streamlit-based web application (app.py) was developed to:

Upload SAR images

Run trained model inference

Display predicted oil spill masks

Show overlay visualization

Deployment Challenges

TensorFlow/Keras version incompatibility

Legacy model serialization issues

To avoid altering finalized training artifacts near submission deadline, deployment was documented but not finalized.

▶️ How to Run the Project (Local)
Step 1: Install Dependencies
pip install -r requirements.txt

Step 2: Run Streamlit App
python -m streamlit run app.py

Step 3: Test Model

Upload a satellite SAR image

View predicted oil spill segmentation

🎯 Project Goals

Automate oil spill detection from satellite imagery

Reduce dependency on manual monitoring

Improve environmental surveillance efficiency

Demonstrate practical application of deep learning in remote sensing

🧠 Key Learnings

SAR image characteristics & challenges

Importance of Dice-based metrics for segmentation

End-to-end ML pipeline design

Real-world deployment constraints in ML systems

👤 Contributor Details
Name	        Role
Piyush Ranjan	Artificial Intelligence Intern

🙏 Acknowledgments

Infosys Springboard Mentor Program

Project Mentor for guidance & review

Zenodo community for dataset resources

Open-source ML ecosystem

🎉 Final Notes

This project demonstrates a complete applied machine learning workflow, from satellite data analysis to model evaluation and visualization.
It highlights both technical depth and practical engineering challenges, making it a strong real-world ML project.