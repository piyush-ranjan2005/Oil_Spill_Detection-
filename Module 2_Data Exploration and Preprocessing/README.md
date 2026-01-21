# 🧪 Module 2: Data Exploration & Preprocessing

## 📌 Module Overview

This notebook focuses on **exploratory data analysis (EDA)** and **preprocessing** of SAR satellite imagery for the **Oil Spill Detection using Deep Learning** project.

After completing **Module 1 (Dataset Collection & Verification)**, this module prepares the dataset for effective training by analyzing image characteristics, normalizing data, resizing inputs, and ensuring masks are correctly formatted for segmentation models.

Notebook file:

```
Module 2_data_exploration_and_preprocessing.ipynb
```

---

## 🎯 Objectives

* Perform exploratory analysis of SAR images and masks
* Visualize image–mask pairs to understand oil spill patterns
* Normalize and resize images for deep learning models
* Convert masks into model-compatible binary format
* Prepare clean NumPy arrays / tensors for training

---

## 📂 Input Dataset

* **Source:** Refined Deep SAR Oil Spill (SOS) Dataset
* **Prepared in:** Module 1
* **Directory Used:**

```
oil_spill_dataset/
├── train/
├── val/
└── test/
```

Each split contains:

* `images/` – SAR satellite images
* `masks/` – Ground truth oil spill segmentation masks

---

## 🔍 Exploratory Data Analysis (EDA)

The notebook performs:

* Random visualization of **SAR images and corresponding masks**
* Inspection of image resolution and aspect ratios
* Analysis of pixel intensity distribution
* Verification of mask alignment and oil spill coverage

This step helps understand **noise, contrast, and oil spill visibility** in SAR data.

---

## 🧹 Preprocessing Steps

The following preprocessing techniques are applied:

* ✔ Image resizing to a fixed input size (model compatible)
* ✔ Pixel value normalization (0–1 range)
* ✔ Conversion of images to NumPy arrays
* ✔ Mask binarization (oil spill vs background)
* ✔ Shape validation for images and masks

These steps ensure compatibility with **CNN / U-Net segmentation architectures**.

---

## 🛠️ Technologies Used

* Python
* NumPy
* OpenCV / PIL
* Matplotlib
* TensorFlow / Keras (data compatibility)

---

## ▶️ How to Run Module 2

1. Ensure **Module 1** is completed and dataset is prepared
2. Verify dataset path:

   ```
   oil_spill_dataset/
   ```
3. Open the notebook:

   ```
   Module 2_data_exploration_and_preprocessing.ipynb
   ```
4. Run all cells sequentially to:

   * Visualize images and masks
   * Apply preprocessing
   * Validate processed outputs

---

## ✅ Output of Module 2

* Preprocessed images and masks
* Verified tensor shapes for deep learning models

---

⭐ This module strengthens the **data foundation** of the project and is critical for achieving accurate and stable oil spill segmentation results.
