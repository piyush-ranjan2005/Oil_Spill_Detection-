# 🌊 AI-Driven System for Oil Spill Identification and Monitoring

<p align="center">
  <strong>
    Deep learning–based oil spill detection and monitoring system using
    Synthetic Aperture Radar (SAR) satellite imagery and U-Net segmentation.
  </strong>
</p>

---

## 📌 Overview
Oil spills pose a severe threat to marine ecosystems, coastal economies, and environmental safety. Traditional oil spill monitoring relies heavily on manual inspection of satellite images, which is time-consuming, error-prone, and difficult to scale for continuous monitoring.

This project presents an **AI-driven system for oil spill identification and monitoring** that automatically detects and segments oil spill regions from **SAR satellite imagery** using **deep learning–based semantic segmentation**. The system enables **pixel-level oil spill localization**, making it suitable for real-world maritime surveillance and environmental monitoring applications.

---

## 🎯 Objectives
- Automate oil spill detection from SAR satellite imagery  
- Perform **pixel-level semantic segmentation** using deep learning  
- Accurately distinguish oil spills from look-alike phenomena  
- Enable **scalable and deployment-ready** monitoring systems  

---

## 🧠 Model Architecture
- **Model:** U-Net (Encoder–Decoder Convolutional Neural Network)  
- **Task:** Binary semantic segmentation (Oil Spill / Background)  
- **Input:** SAR satellite images  
- **Output:** Binary segmentation mask indicating oil-contaminated regions  

U-Net is selected due to its strong spatial localization capability and robustness against noise in SAR imagery.

---

## ⚙️ Detailed Work Completed

### 1️⃣ Dataset Preparation
- Collected open-source **SAR satellite oil spill datasets**
- Preprocessing steps included:
  - Image resizing to a fixed resolution
  - Pixel value normalization
  - Alignment of SAR images with corresponding ground truth masks

---

### 2️⃣ Model Development
- Designed and implemented a **U-Net architecture** using TensorFlow and Keras
- Encoder extracts hierarchical spatial features
- Decoder reconstructs pixel-level segmentation masks
- Used **Binary Cross-Entropy and Dice Loss** for effective segmentation

---

### 3️⃣ Training and Evaluation
- Trained the model on labeled SAR oil spill data
- Evaluated using standard segmentation metrics:
  - **Dice Coefficient**
  - **Intersection over Union (IoU)**

📊 **Performance Metrics**
- **Mean Dice Score:** ~0.70  
- **Mean IoU:** ~0.57  

The model demonstrated stable and reliable performance on noisy SAR imagery.

---

### 4️⃣ Model Inference and Visualization
- Generated:
  - Binary oil spill segmentation masks
  - Probability heatmaps showing oil spill confidence
- Visualized predictions using Matplotlib and Streamlit

---

### 5️⃣ Deployment
- Deployed the trained model using **Streamlit**
- Provides real-time oil spill detection from uploaded SAR images
- User-friendly interface for visualization and interpretation

---

## 🌐 Deployment Link (Mandatory)
🔗 **Live Application:**  
👉 **https://huggingface.co/spaces/Sachin-007/AI-Driven-Oil-Spill-Detection-and-Monitoring**


---

## 📸 Model Testing & Results (Screenshots)

### 🔹 Input SAR Image
Original SAR satellite image provided to the model.

<img width="256" height="256" alt="Image" src="https://github.com/user-attachments/assets/1660a295-fe4d-4719-a227-22993401a1fd" />
<img width="256" height="256" alt="Image" src="https://github.com/user-attachments/assets/672cef27-56bd-4af3-9f5c-a6d52158b6ea" />
<img width="256" height="256" alt="Image" src="https://github.com/user-attachments/assets/28bba3c3-1559-4277-954e-313d4e290059" />


### 🔹 Ground Truth Mask
Manually labeled oil spill regions used for training and validation.

<img width="256" height="256" alt="Image" src="https://github.com/user-attachments/assets/6450d3ec-c2b2-4a16-b560-b3b9f4123ab9" />
<img width="256" height="256" alt="Image" src="https://github.com/user-attachments/assets/dd195521-f0db-4d69-9534-56ca44f6eeac" />
<img width="256" height="256" alt="Image" src="https://github.com/user-attachments/assets/9d17e94c-63e8-47a4-a009-8210937b2ec5" />


### 🔹 Probability Heatmap
Visualization showing confidence levels of oil spill detection.

<img width="256" height="256" alt="Image" src="https://github.com/user-attachments/assets/6719ed7d-b848-4964-97be-838dbed65029" />
<img width="256" height="256" alt="Image" src="https://github.com/user-attachments/assets/757f0c1c-2a61-4bf4-89d4-0d23f5b6345c" />
<img width="256" height="256" alt="Image" src="https://github.com/user-attachments/assets/3fd2ac62-2be9-40ec-ab4b-9c0c7243ca57" />



> These screenshots demonstrate the model’s ability to accurately detect and localize oil spill regions at the pixel level.

---

## 🛠 Tech Stack
- **Programming Language:** Python  
- **Deep Learning Framework:** TensorFlow / Keras  
- **Libraries:** OpenCV, NumPy, Matplotlib  
- **Web Framework:** Streamlit  
- **Deployment Platform:** Hugging Face / Streamlit Cloud  

---

## 🚀 How to Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 🔮 Future Improvements

<ul>
  <li>Attention U-Net for enhanced boundary detection</li>
  <li>GIS-based oil spill localization</li>
  <li>Temporal analysis to track oil spill spread over time</li>
  <li>Integration with real-time satellite data pipelines</li>
</ul>

---

## 👨‍💻 Author

<p>Sachin Sharma A</p>
<p>AI / Machine Learning Enthusiast</p>

<p>Passionate about building practical, AI-driven deep learning systems with real-world environmental impact.</p>

---

## 📜 License

<p>This project is licensed under the MIT License.</p>

---

<h4 align="center">⭐ If you find this project useful or interesting, please give it a star — it really helps and motivates further improvements!</h4>
