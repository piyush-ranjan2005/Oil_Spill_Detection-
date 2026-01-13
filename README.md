# 🌊 AI-Driven Oil Spill Detection System (SAR Imagery)

An AI-powered deep learning system for detecting and segmenting oil spills in **Synthetic Aperture Radar (SAR)** satellite images using semantic segmentation techniques.

---

## Project Overview

Oil spills pose a serious threat to marine ecosystems, coastal economies, and environmental safety. Traditional oil spill monitoring methods are often manual, time-consuming, and error-prone.

This project presents an **automated oil spill detection system** that leverages **deep learning–based semantic segmentation** to accurately identify oil spill regions from SAR images, enabling faster and more reliable monitoring.

---

## Objectives

- Detect oil spill regions from SAR satellite imagery
- Perform pixel-wise segmentation of oil spill areas
- Reduce manual monitoring effort using AI
- Provide a simple web interface for prediction and visualization

---

## Model & Approach

- **Model Architecture**: Attention U-Net
- **Input**: SAR satellite images
- **Output**: Binary segmentation mask highlighting oil spill regions
- **Loss Function**: Dice Loss 
- **Framework**: PyTorch

---

## Technologies Used

### Programming Languages
- Python

### Libraries & Frameworks
- PyTorch
- NumPy
- OpenCV
- Matplotlib
- PIL (Python Imaging Library)
- Streamlit

---

## Features

- Semantic segmentation of oil spills from SAR images
- Deep learning–based automated detection
- Streamlit-based interactive web application
- Visualization of original image and predicted mask
- Supports real-time image upload and inference

---

## Web Application (Streamlit)

- Upload a SAR image
- Model predicts oil spill regions
- Displays segmented output for easy interpretation

---

## Project Structure
```
oil-spill-detection/
│
├── pycache/ # Python cache files
├── .gitattributes # Git LFS tracking for large model files
├── LICENSE # Project license
├── README.md # Project documentation
│
├── app.py # Streamlit web application
├── model.py # Attention U-Net model architecture
├── attention_unet.pth # Trained model weights (Git LFS)
│
├── oilspilldetection.ipynb # Model training notebook (Colab)
├── Untitled4.ipynb # EDA & preprocessing notebook
│
├── requirements.txt # Python dependencies
└── runtime.txt # Runtime configuration (for deployment)


```
---
## Result and Visualization

https://github.com/user-attachments/assets/ab8dcf21-6272-44aa-8576-1921bc15f0c6





## How to Run the Project

1. Clone the repository
```bash
git clone https://github.com/your-username/oil-spill-detection.git
```

2. Install dependencies
```
pip install -r requirements.txt
```

3. Run the Streamlit app
```
streamlit run app.py
```
---

## Deployable Link
https://oilspilldetection.streamlit.app/

---
## Future Enhancements

- Improve model accuracy using larger datasets
- Multi-class segmentation for different ocean phenomena
- Integration with real-time satellite data
- Deployment on cloud platforms
- Add time-series monitoring and alerts

## Use Cases

- Marine pollution monitoring
- Environmental protection agencies
- Disaster management systems
- Coastal surveillance

---
## Author
Leisha Jain

## License
This project is for academic and research purposes.
