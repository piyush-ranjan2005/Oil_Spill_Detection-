# 🌐 Module 6: Deployment – Oil Spill Detection Web Application

## 📌 Objective

Module 6 focuses on **deploying the trained deep learning model** as a **real-time web application**. This module converts the fine-tuned oil spill segmentation model into a **production-style inference system** that allows users to upload satellite images and instantly visualize oil spill detection results.

This module demonstrates **industry-standard ML deployment practices**, clearly separating **model training** from **model inference**.

---

## 🔁 Model Used (From Module 5)

This module **reuses the fine-tuned U-Net model** saved in Module 5.

* **Model architecture:** U-Net (Segmentation)
* **Framework:** TensorFlow / Keras
* **Model format:** `.keras`
* **File name:**

```
oil_spill_unet_finetuned.keras
```

✔ The model is **not retrained** in Module 6
✔ Only **inference and visualization** are performed
✔ Follows real-world **ML deployment best practices**

---

## 🧠 Technologies Used

* **TensorFlow / Keras** – Model loading and inference
* **Streamlit** – Web application frontend
* **OpenCV** – Image preprocessing
* **Matplotlib** – Visualization
* **NumPy** – Data handling

---

## 📂 Project Structure

```
module_6_deployment/
│
├── app.py                          # Streamlit web application
├── utils.py                        # Inference & visualization functions
├── oil_spill_unet_finetuned.keras  # Trained model from Module 5
├── requirements.txt                # Python dependencies
└── README.md                       # Documentation
```

---

## ⚙️ Application Features

### 🔹 1. Image Upload

* Accepts satellite images in:

  * JPG
  * JPEG
  * PNG

---

### 🔹 2. Real-Time Inference

* Uses the **fine-tuned U-Net model** from Module 5
* Performs **pixel-wise oil spill segmentation**
* No retraining during deployment

---

### 🔹 3. Visualization Outputs

The application displays:

* Original satellite image
* Predicted oil spill segmentation mask
* Overlay of predicted mask on the input image

---

### 🔹 4. Oil Spill Alert System

* Calculates **oil spill area percentage**
* Displays:

  * ⚠️ *Oil Spill Detected* (if spill present)
  * ✅ *No Significant Oil Spill Detected*

This feature supports **decision-making and monitoring workflows**.

---

### 🔹 5. Download Results

Users can download:

* Predicted binary oil spill mask (`.png`)

This is useful for:

* Environmental reports
* Research documentation
* Monitoring systems

---

## 🚀 How to Run the Application

### Step 1: Install Dependencies

```
pip install -r requirements.txt
```

### Step 2: Run Streamlit App

```
streamlit run app.py
```

### Step 3: Open in Browser

```
http://localhost:8501
```

---

## 🌐 Deployment

The application can be deployed using **Streamlit Community Cloud**, enabling:

✔ Public access via URL
✔ Easy sharing for demos and reviews
✔ No server configuration required

---

⭐ This module transforms the project from a research prototype into a **deployable AI solution**.
