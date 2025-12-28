# Module 1: Data Collection & Dataset Preparation

## Dataset Used
Refined Deep SAR Oil Spill (SOS) Dataset  
Source: Zenodo

This dataset contains SAR satellite images and corresponding segmentation masks for oil spill detection and monitoring.

## Satellite Sources
- Sentinel-1 SAR
- PALSAR SAR

## Dataset Structure
The dataset is organized into:
- Training set
- Validation set
- Test set

Each split contains:
- Images (SAR satellite imagery)
- Masks (ground truth oil spill segmentation)

## Dataset Access
Due to size limitations, the dataset is not uploaded to GitHub.

🔗 Google Drive Link:  
https://drive.google.com/drive/folders/1PbM5nRWOpSeblyZBd4oiiAv9vP1RsbT1?usp=sharing

## Preprocessing & Verification
- Removed macOS system files (`.DS_Store`, `._*`, `__MACOSX`)
- Verified image–mask pairing
- Created train / validation / test split
- Automated dataset verification using Python

## How to use? 
- Download the dataset from the Google Drive link
- Extract it into a folder named oil_spill_dataset
- Open dataset_setup.ipynb
- Run all cells to:
Clean unwanted files
Verify image–mask matching
Create test split (15%)
Validate dataset integrity

## Output of Module 1
Clean and verified dataset
Proper train / validation / test split
Dataset ready for preprocessing and model training
