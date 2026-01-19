# Module 2: Data Exploration and Data Preprocessing

## 📌 Objective
This module focuses on understanding and preparing Sentinel-1 SAR satellite data for oil spill detection. The goal is to analyze image characteristics and apply preprocessing techniques to make the dataset suitable for deep learning–based segmentation models.

---

## 📂 Dataset Overview
- **Dataset Source:** Oil Spill Detection Dataset (Zenodo)
- **Satellite Type:** Sentinel-1 SAR
- **Data Organization (Module 1):**
  - Sentinel_SAR_Part 1: Oil spill images with masks
  - Sentinel_SAR_Part 2: No-oil and look-alike images with masks
  - Sentinel_SAR_Part 3: Test images with ground truth (used later)

> ⚠️ The dataset is stored in Google Drive and is not included in this repository due to size constraints.

---

## 🔍 Data Exploration
- Visualized SAR images and corresponding segmentation masks
- Analyzed pixel intensity distribution of spill and non-spill regions
- Studied SAR-specific characteristics such as speckle noise

---

## 🧹 Data Preprocessing
The following preprocessing steps were applied:

- **Speckle Noise Reduction:** Median filtering
- **Resizing:** All images and masks resized to 256×256
- **Normalization:** Pixel values scaled to the range [0, 1]
- **Data Augmentation:**
  - Horizontal and vertical flipping
  - Rotation
  - Brightness and contrast adjustment

These steps improve model robustness and generalization.

---

## 🛠 Tools & Libraries
- Python
- OpenCV
- NumPy
- Matplotlib
- Albumentations
- scikit-image

---

## 📊 Sample Outputs
Sample visualizations generated during preprocessing are available in:

