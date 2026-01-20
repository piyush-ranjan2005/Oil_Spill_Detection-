
# 🌊 AI-Based Oil Spill Detection from SAR Satellite Imagery (Enhanced V2)

A deep learning–based semantic segmentation project for **accurate oil spill detection** from SAR satellite images using an **enhanced U-Net architecture**, **Focal Dice Loss**, higher-resolution inputs, and **Test Time Augmentation (TTA)** to achieve strong IoU performance.

---

## 📋 Table of Contents

* [Project Overview](#project-overview)
* [Key Features](#key-features)
* [Project Architecture](#project-architecture)
* [Implementation Details](#implementation-details)
* [Dataset](#dataset)
* [Training & Evaluation](#training--evaluation)
* [Results & Visualizations](#results--visualizations)
* [Project Structure](#project-structure)
* [Technologies Used](#technologies-used)
* [Future Enhancements](#future-enhancements)

---

## 🎯 Project Overview

Oil spills pose severe threats to marine ecosystems and coastal regions. Manual analysis of satellite imagery is slow, expensive, and prone to error—especially in noisy SAR images.

This project presents an **AI-driven oil spill detection system** that:

* ✅ Automatically segments oil spill regions at pixel level
* ✅ Handles SAR speckle noise effectively
* ✅ Addresses extreme class imbalance
* ✅ Produces accurate and smooth segmentation masks
* ✅ Achieves **IoU ≥ 75% target performance**

The entire pipeline is implemented and validated in a **Google Colab notebook**, making it reproducible and GitHub-friendly.

---

## ⭐ Key Features

### 🔬 Technical Highlights

* **Enhanced U-Net Architecture** for binary segmentation
* **Focal Dice Loss** to handle oil–background imbalance
* **Higher Input Resolution (320×320)** for better boundary detection
* **Test Time Augmentation (TTA)** for robust inference
* **IoU-driven evaluation strategy**

### 📊 Model Capabilities

* Detects oil spills of varying sizes and shapes
* Maintains high recall with controlled false positives
* Produces clean masks despite SAR noise
* Suitable for environmental monitoring and research use

---

## 🏗️ Project Architecture

The project follows a complete deep learning pipeline:

```
Data Collection → Preprocessing → Model Design → Training → Evaluation → Visualization
```

### System Workflow

```
SAR Satellite Image
        ↓
Preprocessing (Resize, Normalize)
        ↓
Enhanced U-Net Model
        ↓
Probability Mask
        ↓
Thresholding + TTA Fusion
        ↓
Final Oil Spill Segmentation
```

---

## 💻 Implementation Details

### 🔹 Data Preprocessing

* Grayscale SAR images
* Resize to **320×320**
* Normalization to [0, 1]
* Binary mask enforcement
* Data augmentation:

  * Horizontal flips
  * Rotations

---

### 🔹 Model Architecture

**Architecture**: Enhanced U-Net

* Encoder–decoder structure
* Skip connections preserve spatial details
* Optimized for binary oil spill segmentation

**Input Shape**: `1 × 320 × 320`
**Output Shape**: `1 × 320 × 320`

---

### 🔹 Loss Function: Focal Dice Loss

Oil spill pixels occupy a very small fraction of SAR images.
To address this imbalance, **Focal Dice Loss** is used:

* Focuses learning on difficult oil pixels
* Penalizes false negatives more strongly
* Improves IoU stability across samples

---

## 📂 Dataset

This project uses a **custom oil spill dataset** hosted on Google Drive.

🔗 **Dataset Download Link**:
[https://drive.google.com/drive/folders/1vk26yHE9akaVGmTs1Qr0PqmowD3PLMKK](https://drive.google.com/drive/folders/1vk26yHE9akaVGmTs1Qr0PqmowD3PLMKK)

### Expected Directory Structure

```
data/
├── train/
│   ├── images/
│   └── masks/
├── val/
│   ├── images/
│   └── masks/
└── test/
    ├── images/
    └── masks/
```

> ⚠️ The dataset is **not included in the repository** due to size constraints.

---
🌐 Streamlit App Deployment & Usage

This project also includes a Streamlit-based web application for interactive oil spill detection.

The app allows you to upload SAR images and visualize predicted oil spill masks directly in the browser.

---

▶️ Run the App Locally

After cloning the repository and installing requirements, run:

streamlit run app.py

You will see output like:

Local URL: http://localhost:8501
Network URL: http://172.28.0.12:8501
External URL: http://35.196.231.118:8501

Open http://localhost:8501 in your browser.

---

🌍 Public Access Using Ngrok (Optional)

If you want to access the app remotely (for demo or sharing):

ngrok http 8501

Example generated public URL:

https://exaggeratingly-claimable-irene.ngrok-free.dev → http://localhost:8501

Open the HTTPS link in any browser to access the app online.

---

⚠️ Common Ngrok Warning & Fix

If you see this warning:

failed to open private leg
connect: connection refused

It usually means Streamlit is not running.

✔️ Fix:

1. First start Streamlit:
streamlit run app.py
2. Then start Ngrok:
ngrok http 8501

Make sure port 8501 is active before launching Ngrok.

---

📌 Important Note

Before running the Streamlit app, ensure you have:

- ✅ Downloaded the dataset
- ✅ Placed it in the correct folder structure
- ✅ Run all improved model code (Enhanced V2)
- ✅ Saved the trained model file (e.g., "model.pth") in the project directory

The app loads the trained model for real-time prediction.

---

🖥️ Example App Output

The Streamlit app displays:

- Uploaded SAR image
- Predicted oil spill mask
- Overlay visualization
- Segmentation results for analysis

This makes the project suitable for demonstrations, research validation, and portfolio presentation.
## 🚀 Training & Evaluation

### Training Configuration

* **Optimizer**: Adam
* **Learning Rate**: 1e-4
* **Loss Function**: Focal Dice Loss
* **Evaluation Metric**: IoU (primary)
* **Target IoU**: ≥ 75%

### Test Time Augmentation (TTA)

During inference:

* Original image
* Augmented variants (flip / rotation)
* Predictions averaged for final output

This improves segmentation smoothness and robustness.

---

## 📊 Evaluation Metrics

The model is evaluated using:

* **Intersection over Union (IoU)**
* **Dice Coefficient**
* **Precision**
* **Recall**

These metrics ensure both detection accuracy and boundary quality.

---

## 🖼️ Results & Visualizations

The notebook includes:

* Input SAR images
* Ground truth masks
* Predicted segmentation masks
* Overlay visualizations
* IoU-based performance analysis

The model demonstrates:

* Strong overlap with ground truth
* High recall for oil spill regions
* Stable predictions across test samples

---

## 📁 Project Structure

```
Oil_Spill_Detection_Enhanced/
│
├── notebooks/
│   └── Oil_Spill_Detection_Enhanced_V2.ipynb
│
├── data/                     # Not included (download separately)
│
├── results/
│   └── sample_predictions.png
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 🛠️ Technologies Used

### Deep Learning

* PyTorch
* NumPy

### Image Processing

* OpenCV
* PIL

### Visualization

* Matplotlib

### Development

* Google Colab
* GitHub

---

## 🚧 Future Enhancements

* Attention U-Net integration
* Multi-scale feature extraction
* Temporal spill monitoring
* Area estimation in km²
* Lightweight inference optimization

---

## 📝 License

This project is licensed under the **MIT License**.

---

## 🙏 Acknowledgments

* SAR imagery from Sentinel-1 (ESA Copernicus)
* Oil Spill Dataset (custom curated)
* PyTorch open-source community

---


---

