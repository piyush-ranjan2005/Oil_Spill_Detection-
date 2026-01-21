# 📦 Module 1: Data Collection & Dataset Preparation

## 🎯 Objective

To collect, clean, verify, and organize SAR satellite imagery datasets for oil spill detection, ensuring correct **image–mask pairing** and a robust **train / validation / test split**.

---

## 📊 Dataset Used

**Refined Deep SAR Oil Spill (SOS) Dataset**
**Source:** Zenodo

This dataset contains **SAR satellite images** along with corresponding **segmentation masks** for accurate oil spill detection and monitoring.

---

## 🛰️ Satellite Sources

* **Sentinel-1 SAR**
* **PALSAR SAR**

These satellites provide high-resolution radar imagery suitable for ocean surface analysis under all weather conditions.

---

## 🗂️ Dataset Structure

The dataset is organized into three splits:

* **Training Set**
* **Validation Set**
* **Test Set**

Each split contains:

* **Images:** SAR satellite imagery
* **Masks:** Ground truth oil spill segmentation masks

Expected directory structure after preparation:

```
oil_spill_dataset/
│
├── train/
│   ├── images/
│   └── masks/
│
├── val/
│   ├── images/
│   └── masks/
│
├── test/
│   ├── images/
│   └── masks/
```

---

## 🔗 Dataset Access

Due to size limitations, the dataset is **not uploaded to GitHub**.

📁 **Google Drive Link:**
[https://drive.google.com/drive/folders/1PbM5nRWOpSeblyZBd4oiiAv9vP1RsbT1?usp=sharing](https://drive.google.com/drive/folders/1PbM5nRWOpSeblyZBd4oiiAv9vP1RsbT1?usp=sharing)

---

## 🧹 Preprocessing & Verification

The following preprocessing and verification steps are automated using Python in `dataset_setup.ipynb`:

* Removed macOS system files (`.DS_Store`, `._*`, `__MACOSX`)
* Verified correct **image–mask pairing**
* Detected missing or mismatched files
* Created **train / validation / test split**

  * Test set size: **15%**
* Validated dataset integrity for deep learning readiness

---

## ▶️ How to Use Module 1

1. Download the dataset from the **Google Drive link**
2. Extract it into a folder named:

   ```
   oil_spill_dataset
   ```
3. Open the notebook:

   ```
   dataset_setup.ipynb
   ```
4. Run all cells to:

   * Clean unwanted system files
   * Verify image–mask matching
   * Create train / validation / test splits
   * Validate dataset integrity

---

## ✅ Output of Module 1

* Clean and verified dataset
* Proper **train / validation / test split**

---

## 🛠️ Technologies Used

* Python
* NumPy
* OS & File Handling
* Matplotlib (for verification & visualization)
* Deep Learning–ready segmentation pipeline

---


⭐ This project is designed to be **resume-ready**, **research-oriented**, and suitable for **hackathons, academic submissions, and real-world environmental monitoring systems**.
