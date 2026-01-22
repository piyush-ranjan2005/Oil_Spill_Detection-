🛢️ Oil Spill Detection Using Satellite SAR Imagery

End-to-End Deep Learning Project (Segmentation-Based Approach)

📌 Project Information
Item	Details
Project Title	Oil Spill Detection Using Satellite Images
Domain	Computer Vision, Remote Sensing, Deep Learning
Technique	Image Segmentation (U-Net)
Satellite Type	Sentinel-1 SAR
Internship Program	Infosys Springboard Mentor Program
Contributor	Piyush Ranjan
Assigned Branch	Piyush-AI-Oil-Spill-Detection
Main Repository	springboardmentor112r-Agri/Oil_Spill_Detection-
📖 Project Overview

Oil spills are one of the most harmful environmental disasters, severely impacting marine ecosystems, coastal economies, and biodiversity. Early detection of oil spills is crucial for rapid response and damage control.

This project implements an end-to-end deep learning pipeline to automatically detect oil spill regions from satellite SAR (Synthetic Aperture Radar) images using semantic segmentation.

Unlike optical images, SAR imagery is robust to:

Cloud cover

Weather conditions

Night-time acquisition

Making it ideal for oil spill monitoring.

🎯 Objectives

The key objectives of this project are:

To analyze and preprocess satellite SAR imagery

To build a deep learning–based segmentation model

To accurately detect oil spill regions

To evaluate performance using segmentation metrics

To visualize predictions clearly

To attempt deployment through a web interface

🗂️ Dataset Description
Attribute	Details
Dataset Name	Oil Spill Detection Dataset (Zenodo)
Satellite Source	Sentinel-1 SAR
Image Type	Grayscale SAR Images
Annotation Type	Binary Segmentation Masks
Resolution (After Processing)	256 × 256
Classes	Oil Spill, Background
Dataset Characteristics

Oil spills appear as dark regions in SAR images due to reduced backscatter.

Look-alike phenomena (low wind zones) make detection challenging.

Segmentation masks label oil spill pixels explicitly.

📁 Repository Structure
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

🧠 Notebook Overview
Notebook	Description
Oil_Spill_Detection_End_to_End.ipynb	Contains Modules 2–5 (Exploration, Preprocessing, Model Development, Training, Evaluation, Visualization)

All core ML work is implemented and validated inside this notebook.

🧱 Module-Wise Implementation
✅ Module 1: Data Collection

Work Completed

Acquired Sentinel-1 SAR imagery from open datasets

Downloaded labeled oil spill segmentation data

Verified image–mask alignment

Organized dataset for ML processing

✅ Module 2: Data Exploration & Preprocessing
🔍 Data Exploration

Visualized sample SAR images and masks

Analyzed pixel intensity distributions

Studied oil vs non-oil backscatter patterns

⚙️ Preprocessing Steps
Step	Description
Resizing	Images resized to 256 × 256
Normalization	Pixel values scaled to [0, 1]
Channel Handling	Single-channel SAR images
Noise Consideration	SAR speckle awareness
🔁 Data Augmentation

Horizontal flipping

Vertical flipping

Rotation

Intensity normalization

✅ Module 3: Model Development (Segmentation)
🧠 Model Architecture

U-Net (Encoder–Decoder)

Skip connections preserve spatial details

Designed for binary segmentation

Component	Description
Input	256 × 256 × 1 (SAR image)
Encoder	Convolution + MaxPooling
Bottleneck	Deep feature extraction
Decoder	Upsampling + Skip Connections
Output	Binary segmentation mask
✅ Module 4: Training & Evaluation
🔧 Training Configuration
Parameter	Value
Loss Function	Dice Loss + Binary Cross-Entropy
Optimizer	Adam
Batch Size	Configured experimentally
Epochs	Tuned for convergence
📊 Evaluation Metrics

Accuracy

Dice Coefficient

Intersection over Union (IoU)

Precision

Recall

Model performance was evaluated on validation data to ensure generalization.

✅ Module 5: Visualization of Results
📷 Visual Outputs

Original SAR image

Ground truth mask

Predicted oil spill mask

Overlay visualization (image + prediction)

Screenshots are stored inside the screenshots/ folder and clearly demonstrate model performance.

📊 Results & Visual Evidence
Visualization	Description
Sample Input	Raw SAR image
Ground Truth	Annotated oil spill mask
Prediction	Model-generated segmentation
Overlay	Combined SAR image + prediction

(Refer to the screenshots/ directory for visual outputs)

🚀 Module 6: Deployment via Streamlit (Status)
⚠️ Status: Attempted & Documented

A Streamlit web application (app.py) was developed to:

Upload satellite images

Run model inference

Display predicted oil spill masks

Show overlay visualizations

However, during deployment, TensorFlow–Keras version incompatibility issues were encountered due to legacy model serialization.

Deployment Link
Deployment attempted but not finalized due to environment compatibility issues.


This decision was taken to avoid modifying the finalized training artifacts close to the deadline.

🖥️ How to Run the Streamlit App (Local)
1️⃣ Install Dependencies
pip install -r requirements.txt

2️⃣ Run the App
python -m streamlit run app.py

3️⃣ Upload Image

Upload a SAR satellite image (PNG/JPG)

View predicted oil spill segmentation

🛠️ Tech Stack Used
Category	Tools
Programming	Python
Deep Learning	TensorFlow, Keras
Image Processing	NumPy, PIL
Visualization	Matplotlib
Deployment	Streamlit
Version Control	Git, GitHub
🧠 Key Learnings

Handling SAR imagery for segmentation

Importance of Dice-based metrics

Challenges in ML deployment pipelines

Real-world compatibility issues in MLOps

End-to-end ML workflow execution

👤 Contributor Details
Name	Role
Piyush Ranjan	Artificial Intelligence Intern
✅ Final Conclusion

This project successfully demonstrates a complete deep learning pipeline for oil spill detection using satellite SAR imagery. It covers data preparation, model development, training, evaluation, and visualization, while also documenting real-world deployment challenges.

The work reflects both technical depth and practical ML engineering awareness.

📌 Acknowledgement

This project was completed under the guidance of the Infosys Springboard Mentor Program.