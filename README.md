AI-Based Oil Spill Detection Using Sentinel-1 SAR Imagery

Project Title: AI-Driven Oil Spill Detection and Monitoring

Author: Kundan Yadav

Domain: Remote Sensing · Deep Learning · Environmental Monitoring

Project Overview

Oil spills pose a serious threat to marine ecosystems and coastal environments. Manual inspection of satellite imagery is slow and inefficient, especially under adverse weather conditions. This project presents an AI-based oil spill detection system using Sentinel-1 Synthetic Aperture Radar (SAR) imagery, designed to automatically localize oil-contaminated regions and support area estimation and early warning for environmental monitoring.

Unlike classification-based approaches, this project focuses on semantic segmentation, producing pixel-level oil masks that can be further used for spatial analysis and impact assessment.

Objectives

Detect oil spill regions in Sentinel-1 SAR imagery

Generate pixel-wise segmentation masks

Support oil spill area estimation (km²)

Evaluate robustness using coastal stress testing

Design a system suitable for early-warning and analyst-in-the-loop monitoring

🧩 Dataset Description
1. Sentinel-1 SAR Dataset (Primary)

2. Sensor: Sentinel-1 (C-band SAR)

Dates used:

Step 1: Download ZIP

Download sense from Alaska SAR Facility (ASF) website

https://search.asf.alaska.edu/#/ 

Aug 09, 2017 – training / validation / primary test

Aug 12, 2017 – training / validation / primary test

Aug 05, 2017 – stress test (coastal-heavy scenes)


Step 2: Preprocessing (SNAP → ML-ready tiles)

(What to do)
SNAP Pipeline:
1. Apply Orbit File
2. Remove Thermal Noise
3. Radiometric Calibration (σ⁰)
4. Speckle Filtering (Refined Lee)
5. Terrain Correction (Range-Doppler)
6. Convert linear to dB
7. Export ML-ready GeoTIFF
8. Build SNAP graph (reuse settings automatically)


(How to do)
Actuall SNAP steps: 
1. Radar → Apply Orbit File
2. Radar → Radiometric → S-1 Thermal Noise Removal
3. Radar → Radiometric → Calibrate
4. Radar → Speckle Filtering → Single Product Speckle Filter
5. Radar → Geometric → Ellipsoid Correction → Average Height Range-Doppler
6. Raster → Data Conversion → Convert bands to/from dB
7. File → Export → GeoTIFF / BigTIFF
8. Tools → Graph Builder → Add nodes in order

Step 3: tilling

Tile size: 400 × 400

Resolution: 10 m × 10 m per pixel

2. Kaggle Dataset

Used only for reference and understanding
Not used in final training or evaluation

✍️ Annotation Details

Tool used: LabelMe
Label: "oil" (single-class segmentation)
Annotation rules:
Only oil regions annotated
Land and ocean background ignored
Clean ocean tiles have empty annotations
Binary masks generated from JSON annotations:
Oil pixels = 255
Background = 0

🧠 Model Architecture

Model: U-Net (baseline)
Input: 1-channel SAR image
Output: 1-channel binary oil mask
Loss function: Binary Cross-Entropy + Dice Loss
Optimizer: Adam (learning rate = 1e-4)

Training epochs: 20

📁 Project Folder Structure
oil_spill_project/
├── data/
│   └── sentinel/
│       └── tiles/
│           ├── train/
│           │   ├── images/
│           │   ├── masks/
│           │   └── annotations/
│           ├── val/
│           │   ├── images/
│           │   ├── masks/
│           │   └── annotations/
│           ├── primary_test/
│           │   ├── images/
│           │   ├── masks/
│           │   └── annotations/
│           └── stress_test/
│               └── images/
├── models/
│   └── best_model.pth
├── notebooks/
│   ├── training.ipynb
│   ├── inference.ipynb
│   └── evaluation.ipynb
├── README.md
└── LICENSE

Evaluation Strategy
Pixel-wise Metrics

Dice and IoU were initially evaluated

Found to be numerically unstable due to extremely sparse oil annotations

Area-Based Evaluation (Primary)

Oil area estimated using predicted masks

Pixel-to-area conversion:

1 pixel = 100 m²

Metrics reported:

Predicted oil area (km²)

Absolute area error

Overestimation ratio

Stress Test

Conducted on 2,712 coastal SAR tiles

Focused on:

Robustness near coastlines

False positives in calm-water regions

Graceful degradation under difficult conditions

📊 Key Results

Primary Test (Open Ocean)

Mean GT oil area: ~0.004 km²

Mean predicted oil area: ~0.37 km²

Model prioritizes high recall and regional localization

Stress Test (Coastal Scenes)

Total tiles: 2,712

Mean predicted oil area: 0.465 km²

Median predicted oil area: 0.266 km²

Max predicted oil area: 2.71 km²

Model remained stable and interpretable under stress

🔍 Key Observations

Pixel-perfect boundary metrics (Dice/IoU) are unsuitable for ultra-thin SAR oil slick annotations

The model functions effectively as an early-warning oil spill localization system

Overestimation is intentional and acceptable for safety-critical environmental monitoring

Stress testing confirms robustness and graceful degradation

📝 Conclusion

This project demonstrates the feasibility of using deep learning–based semantic segmentation for oil spill detection in Sentinel-1 SAR imagery. While precise boundary delineation remains challenging due to annotation sparsity and SAR look-alikes, the proposed system reliably identifies oil-prone regions and provides useful area estimates. The results highlight the importance of aligning evaluation metrics with operational objectives in real-world environmental monitoring applications.
