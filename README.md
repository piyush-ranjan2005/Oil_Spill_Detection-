📂 Project Structure
oil-spill-detection/
│
├── model.py                 # UNet architecture
├── app.py                   # Streamlit inference app
├── sar_unet_model.pth       # Trained model weights
├── requirements.txt         # Dependencies
├── images/                  # (Add your result images here)
│   ├── raw_sar.png
│   ├── ground_truth.png
│   ├── predicted_mask.png
│   └── overlay.png
└── README.md

🔍 Exploratory Data Analysis (EDA)

Visual inspection of SAR images and masks

Shape & datatype verification

SAR noise (speckle) analysis using:

Pixel intensity histograms

Zoomed texture patches

Overlay visualization to verify mask alignment

Key Insight:
Oil spills appear as dark, smooth regions in SAR due to reduced backscatter.

⚙️ Preprocessing Pipeline (SAR-Specific)

Applied consistently during training and inference:

Convert to grayscale (if needed)

Resize to 256 × 256

Normalize pixel values

Median filtering (speckle noise reduction)

CLAHE (contrast enhancement)

Final normalization to [0, 1]

Resize → Denoise → CLAHE → Normalize

🔄 Data Augmentation

To improve generalization:

Horizontal flip

90° rotation

This helps the model learn orientation-invariant features.

🧬 Model Architecture – UNet

Encoder–decoder structure

Skip connections preserve spatial details

Designed for binary segmentation

Output classes:

0 → Background

1 → Oil Spill

Loss Function

Combined loss for stability and accuracy:

Total Loss = CrossEntropyLoss + DiceLoss


Dice Loss helps handle class imbalance common in oil spill datasets.

🚀 Training Details

Framework: PyTorch

Optimizer: Adam

Learning Rate: 1e-4

Batch Size: 8

Train / Validation Split: 80 / 20

Model saved as: sar_unet_model.pth

🧪 Inference & Deployment (Streamlit)

The project includes a Streamlit web app for easy testing.

App Features:

Upload SAR image (.png, .jpg)

Preprocessing identical to training

Real-time segmentation

Visual comparison:

Original Image

Preprocessed Image

Predicted Mask

Run the App
streamlit run app.py

📦 Installation
1️⃣ Clone Repository
git clone https://github.com/your-username/oil-spill-detection.git
cd oil-spill-detection

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run Streamlit App
streamlit run app.py

🧾 Requirements
torch>=2.0.0
torchvision>=0.15.0
streamlit>=1.30.0
opencv-python-headless>=4.8.0
numpy>=1.23.0
Pillow>=9.5.0
