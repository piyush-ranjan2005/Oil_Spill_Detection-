# 🛢️ Oil Spill Detection Using SAR Images (UNet)

Deep Learning–based Semantic Segmentation of Oil Spills from Synthetic Aperture Radar (SAR) Images using UNet.

---

## 📌 Project Overview

Oil spills cause severe environmental damage and require fast, reliable monitoring.  
This project implements a **UNet-based deep learning model** to detect and segment oil spills from **SAR images**, which are widely used because they:

- Work day and night  
- Are weather independent  
- Highlight oil spills due to backscatter differences  

The project covers the **complete pipeline**:
- Exploratory Data Analysis (EDA)
- SAR-specific preprocessing
- Data augmentation
- UNet model training
- Model saving and loading
- Deployment using Streamlit

---

## 🛰️ Sample Outputs (Replace with Your Images)

### Raw SAR Image
![Raw SAR Image](images/raw_sar.png)

### Ground Truth Mask
![Ground Truth Mask](images/ground_truth.png)

### Predicted Oil Spill Mask
![Predicted Mask](images/predicted_mask.png)

### Overlay Visualization
![Overlay Result](images/overlay.png)

> 📌 Create an `images/` folder and replace these images with your results.

---

## 🧠 Key Features

- SAR-specific preprocessing (Median Filter + CLAHE)
- Custom UNet architecture implemented in PyTorch
- Dice Loss + Cross Entropy Loss
- Custom Dataset and DataLoader
- Data augmentation for robustness
- Streamlit-based inference UI
- CPU and GPU compatible

---

## 📂 Project Structure

```text
oil-spill-detection/
├── model.py
├── app.py
├── sar_unet_model.pth
├── requirements.txt
├── images/
│   ├── raw_sar.png
│   ├── ground_truth.png
│   ├── predicted_mask.png
│   └── overlay.png
└── README.md
```

---

## 🔍 Exploratory Data Analysis (EDA)

EDA includes:
- Visual inspection of SAR images and masks
- Shape and datatype verification
- SAR speckle noise analysis using histograms
- Zoomed texture patches
- Overlay visualization to verify image–mask alignment

Oil spills appear as **dark, smooth regions** in SAR images due to reduced backscatter.

---

## ⚙️ Preprocessing Pipeline

The same preprocessing is applied during **training and inference**.

Steps:
1. Convert to grayscale (if required)
2. Resize to `256 × 256`
3. Normalize intensity values
4. Median filtering (speckle noise reduction)
5. CLAHE (contrast enhancement)
6. Final normalization to `[0, 1]`


---

## 🔄 Data Augmentation

To improve generalization:
- Horizontal flip
- 90-degree rotation

This helps the model handle orientation variations in SAR data.

---

## 🧬 Model Architecture (UNet)

- Encoder–decoder architecture
- Skip connections preserve spatial information
- Binary segmentation output

### Output Classes
- `0` → Background
- `1` → Oil Spill

### Loss Function

Combined loss:
Total Loss = CrossEntropyLoss + DiceLoss


Dice Loss helps handle class imbalance common in oil spill datasets.

---

## 🚀 Training Details

- Framework: PyTorch
- Optimizer: Adam
- Learning Rate: `1e-4`
- Batch Size: `8`
- Train/Validation Split: `80/20`
- Model saved as: `sar_unet_model.pth`

---

## 🧪 Streamlit Inference App

The Streamlit app allows interactive testing.

### Features
- Upload SAR images (`png`, `jpg`, `jpeg`)
- Real-time preprocessing
- Oil spill segmentation
- Side-by-side visualization:
  - Original image
  - Preprocessed image
  - Predicted mask

### Run the App

```bash
streamlit run app.py
