# 🌊 OilWatch AI 🛢️

**AI-Driven Oil Spill Identification and Monitoring System using Satellite Imagery and Deep Learning**
<img width="1361" height="527" alt="Screenshot 2026-01-21 143036" src="https://github.com/user-attachments/assets/196eb5af-3df6-4279-9930-81cd3c56d413" />


---

## **Project Overview**

**OilWatch AI** is an AI-driven system that automatically detects and segments oil spills in satellite imagery using deep learning models like **CNN** and **U-Net**.  
It provides environmental monitoring agencies with a **fast, accurate, and automated solution**, reducing reliance on slow and error-prone manual inspections.  

---

## **Problem Statement**

Oil spills pose **serious environmental and economic hazards**, impacting marine ecosystems and local economies.  
Traditional monitoring methods rely on **manual satellite image analysis**, which is:  

- ⏳ **Time-consuming**  
- ⚠️ **Error-prone**  
- 📉 **Inefficient for large-scale monitoring**  

**Solution:** Develop an automated system that detects oil spills and generates **pixel-level segmentation masks** from satellite images for **near real-time monitoring**.  

---

## **Solution Overview**

OilWatch AI leverages **satellite SAR imagery** (Sentinel-1, PALSAR) and **deep learning models** (CNN, U-Net) to:  

- Automatically detect oil spills in satellite images  
- Produce **pixel-level segmentation masks** of contaminated regions  
- Visualize and highlight affected areas  
- Deploy a **web interface** for easy, real-time monitoring  

This system is accessible via **Streamlit or Flask**, enabling environmental agencies to use it **without technical expertise**.  

**Deployment Link:** [OilWatch AI Web App]([https://your-deployment-link.com](https://oilwatch-ai.streamlit.app/) 
---

## **Key Features**

- ✅ Automatic detection of oil spills from satellite images  
- ✅ Pixel-level segmentation of contaminated regions  
- ✅ Deep learning-based pattern recognition for high accuracy  
- ✅ Real-time visualization of affected areas  
- ✅ User-friendly web deployment for monitoring and analysis  

---

## **Tech Stack**

| Component                | Technology / Tool                                           |
|--------------------------|-------------------------------------------------------------|
| Programming Language     | Python                                                      |
| Deep Learning Models     | CNN, U-Net                                                  |
| Satellite Data           | Sentinel-1, PALSAR SAR imagery                               |
| Dataset                  | Refined Deep SAR Oil Spill (SOS) Dataset by Zenedo         |
| Visualization & Deployment | Matplotlib, OpenCV, Streamlit, Flask                       |
| Image Processing         | PIL, NumPy                                                  |

---

## **Detailed Work Completed**

The project was developed in **7 major stages**:  

### **1. Data Collection**
- Collected SAR satellite images (Sentinel-1, PALSAR)  
- Integrated the **Refined Deep SAR Oil Spill (SOS) Dataset** with pixel-level segmentation masks  

### **2. Exploratory Data Analysis (EDA)**
- Visualized sample images and masks  
- Analyzed patterns in oil-contaminated regions  
- Checked dataset quality and class distribution  

### **3. Data Preprocessing**
- Normalized and resized images for model compatibility  
- Augmented dataset using rotations, flips, and intensity adjustments  
- Prepared segmentation masks aligned with input images  

### **4. Model Development**
- **CNN:** Extracted visual features and patterns of oil spills  
- **U-Net:** Pixel-level segmentation for accurate highlighting of affected regions  

### **5. Training and Evaluation**
- Trained models using **cross-entropy** and **Dice loss**  
- Evaluated performance using **IoU**, **Dice coefficient**, and **accuracy**  
- Tuned hyperparameters for optimal segmentation accuracy  

### **6. Visualization of Results**
- Overlaid predicted segmentation masks on original satellite images  
- Generated clear, interpretable visuals for monitoring and reporting  

### **7. Deployment**
- Developed a **Streamlit web app** for user-friendly interaction  
- Users can upload satellite images and receive **real-time oil spill segmentation**  
- Ensured smooth visualization and fast inference for practical use  

---

## **Project Modules**

- **Data Collection & EDA** – Gathering and analyzing satellite data  
- **Preprocessing** – Normalization, augmentation, and mask preparation  
- **Modeling** – CNN & U-Net for detection and segmentation  
- **Training & Evaluation** – Model optimization and metric analysis  
- **Visualization** – Overlaying masks on images for clear interpretation  
- **Deployment** – Streamlit/Flask web interface for real-time usage  

---

## **How to Run**

**Prerequisites:**  

- Python 3.8+  
- Required libraries: `tensorflow`, `opencv-python`, `Pillow`, `matplotlib`, `streamlit`  

**Steps:**  

1. Clone the repository:  
```bash
git clone <repository-url>
cd OilWatch-AI
```
2.Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the web app (Streamlit example):
```
streamlit run app.py
```
4 .Upload satellite images through the interface to detect oil spills and view segmentation masks.

Deployment Link: https://oilwatch-ai.streamlit.app/
<img width="1364" height="673" alt="Screenshot 2026-01-21 143013" src="https://github.com/user-attachments/assets/cf1325cb-9b2b-46e7-8dff-a91a48784f99" />
Oil Spill Detected
<img width="1365" height="675" alt="Screenshot 2026-01-21 143100" src="https://github.com/user-attachments/assets/27b3836a-a146-43e6-8c6f-7e60152bf346" />
No Oil Spill Detected

---
## **Future Enhancements**

1. Integrate real-time satellite feed for continuous monitoring
2. Add multi-spectral analysis to improve detection accuracy
3. Enable historical trend analysis for oil spill patterns
4. Develop a mobile version for on-field monitoring

---

Acknowledgements: 
This project is developed as part of the Infosys Springboard Internship program.
Dataset: Refined Deep SAR Oil Spill (SOS) Dataset by Zenedo
Inspired by research on oil spill detection using deep learning and SAR imagery

---
