🛢️ AI-Driven Oil Spill Detection Using Satellite SAR Imagery

Automated Environmental Monitoring with Deep Learning & Remote Sensing

“Detecting environmental disasters before they escalate.”


📚 Table of Contents

What Is This?

Why This Project Exists

Features That Matter

System Architecture

Tech Stack

Dataset Overview

Project Structure

Notebook Walkthrough

Model & Training

Results & Visualizations

Deployment Status

How to Run

Key Learnings

Project Goals

Contributor

Acknowledgments

Final Words

🤔 What Is This?

This project is an AI-powered oil spill detection system that uses Satellite SAR imagery and deep learning-based image segmentation to automatically identify oil spill regions in marine environments.

Unlike traditional manual inspection methods, this system:

Works in all weather conditions

Detects oil spills at pixel-level accuracy

Enables scalable and automated monitoring

💡 Why This Project Exists

Oil spill monitoring in the real world suffers from multiple limitations:

Manual satellite image inspection is slow and subjective

Optical images fail due to clouds and lighting

Look-alike patterns confuse classical algorithms

Delayed detection causes irreversible damage

This project solves these problems using:

SAR satellite data

Deep learning segmentation (U-Net)

Robust preprocessing & evaluation

✨ Features That Matter
🔍 Automated Oil Spill Detection

Detects oil spill regions directly from SAR satellite images.

🧠 Deep Learning Segmentation

Uses a U-Net architecture optimized for binary segmentation.

🖼️ Visual Interpretability

Shows:

Original SAR image

Ground truth mask

Predicted mask

Overlay visualization

📊 Performance Evaluation

Measures model quality using:

Dice Coefficient

IoU

Accuracy, Precision & Recall

🌐 Deployment-Ready Design

Includes a Streamlit-based UI for interactive testing.

🏗️ System Architecture

High-level flow:

SAR satellite image input

Image preprocessing & normalization

U-Net model inference

Segmentation mask prediction

Visualization & analysis

🛠️ Tech Stack
| Layer            | Technology        | Why It’s Used              |
| ---------------- | ----------------- | -------------------------- |
| Programming      | Python            | Core implementation        |
| Deep Learning    | TensorFlow, Keras | Model training & inference |
| Image Processing | NumPy, PIL        | SAR image handling         |
| Visualization    | Matplotlib        | Clear visual outputs       |
| Deployment       | Streamlit         | Fast web UI                |
| Version Control  | Git & GitHub      | Collaboration & review     |

🗂️ Dataset Overview
| Attribute  | Details                    |
| ---------- | -------------------------- |
| Source     | Kaggle (Oil Spill Dataset) |
| Satellite  | Sentinel-1 SAR             |
| Image Type | Grayscale SAR              |
| Labels     | Binary segmentation masks  |
| Classes    | Oil Spill, Background      |
| Resolution | 256 × 256                  |

Why SAR?

Weather-independent

Detects surface roughness

Ideal for maritime monitoring

📁 Project Structure
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
│   ├── ground_truth_mask.png
│   ├── predicted_mask.png
│   └── overlay_visualization.png
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore

📓 Notebook Walkthrough

The notebook Oil_Spill_Detection_End_to_End.ipynb covers:

Data exploration

Preprocessing

Model design

Training & validation

Evaluation & visualization

🧠 Model & Training

Architecture: U-Net

Loss: Dice Loss + Binary Cross-Entropy

Optimizer: Adam

Task: Binary image segmentation

Evaluation Metrics

Dice Coefficient

IoU

Accuracy

Precision & Recall

📊 Results & Visualizations

The screenshots/ folder contains:

Raw SAR image

Ground truth mask

Model prediction

Overlay visualization

These visuals clearly demonstrate the model’s segmentation quality.

🚀 Deployment Status

⚠️ Deployment: Attempted & Documented

A Streamlit app (app.py) was built to:

Upload SAR images

Run inference

Display predicted masks

Challenge faced:
TensorFlow/Keras version incompatibility with saved model.

To avoid last-minute retraining, deployment was documented but not finalized.

▶️ How to Run

pip install -r requirements.txt
python -m streamlit run app.py

Upload a SAR image and view the predicted oil spill mask.

🧠 Key Learnings

Understanding SAR image characteristics

Importance of Dice-based metrics

End-to-end ML pipeline design

Real-world ML deployment constraints

🎯 Project Goals

Automate oil spill detection

Reduce manual monitoring effort

Improve environmental response time

Apply deep learning to remote sensing

👤 Contributor

| Name              | Role                    |
| ----------------- | ----------------------- |
| **Piyush Ranjan** | Machine Learning Intern |

🙏 Acknowledgments

Springboard Mentor Program

Project mentor for guidance

Kaggle community

Open-source ML ecosystem

🎉 Final Words

This project represents a complete real-world machine learning pipeline, combining satellite data, deep learning, evaluation, and deployment considerations.

It reflects both technical depth and practical engineering challenges.



