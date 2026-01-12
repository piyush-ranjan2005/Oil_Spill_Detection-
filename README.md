# 🌊 AI-Driven System for Oil Spill Identification and Monitoring

<p align="center">
  <strong>
    Deep learning–based oil spill detection and monitoring system using
    Synthetic Aperture Radar (SAR) satellite imagery and U-Net segmentation.
  </strong>
</p>

---

## 📌 Overview
Oil spills pose a serious threat to marine ecosystems, coastal economies, and environmental safety. Conventional oil spill monitoring relies heavily on manual inspection of satellite images, which is slow, error-prone, and difficult to scale.

This project presents an **AI-driven system for oil spill identification and monitoring** that automatically detects and segments oil spill regions from **SAR satellite imagery** using **deep learning**. The system performs **pixel-level semantic segmentation**, enabling precise localization of oil-contaminated areas and supporting real-time maritime surveillance.

---

## 🎯 Objectives
- Automate oil spill detection from satellite imagery  
- Perform **pixel-level segmentation** using deep learning  
- Improve detection accuracy over traditional image-processing methods  
- Enable **scalable and deployment-ready** monitoring for real-world use  

---

## 🧠 Model
- **Architecture:** U-Net (Encoder–Decoder CNN)  
- **Task:** Binary semantic segmentation (Oil / Non-oil)  
- **Input:** SAR satellite images  
- **Output:** Binary oil spill mask  

U-Net is chosen for its strong spatial localization capability and effectiveness in segmentation tasks involving complex and noisy data.

---

## ⚙️ Workflow
1. Preprocess SAR images (resize and normalize)  
2. Apply the U-Net model for segmentation  
3. Generate binary masks and probability maps  
4. Visualize results through a web-based dashboard  

---

## 📊 Results
- **Mean Dice Score:** ~0.70  
- **Mean IoU:** ~0.57  
- Stable and reliable performance on noisy SAR imagery  

---

## 🌐 Application Features
- SAR image upload interface  
- Oil spill segmentation mask visualization  
- Probability heatmap generation  
- Confidence estimation for predictions  
- Real-time inference using Streamlit  

---

## 🛠 Tech Stack
- **Language:** Python  
- **Framework:** TensorFlow / Keras  
- **Libraries:** OpenCV, NumPy, Matplotlib  
- **Deployment:** Streamlit, Hugging Face  

---

## 🚀 How to Run
```bash
pip install -r requirements.txt
streamlit run app.py
```
---

## 🔮Future Improvements
<ul> 
  <li>Attention U-Net for improved boundary detection</li> 
  <li>GIS-based oil spill localization</li>
  <li>Temporal tracking of oil spill spread over time</li>
</ul>

---

## 👨‍💻 Author

<b>Sachin Sharma A</b>
<h5>AI / Machine Learning Enthusiast</h5>

Passionate about building practical, AI-driven deep learning systems with real-world impact.

---

## 📜 License

This project is licensed under the <b>MIT License</b>.

---

<h4 align="center">⭐ If you find this project useful or interesting, please give it a star — it really helps and motivates further improvements!</h4>
