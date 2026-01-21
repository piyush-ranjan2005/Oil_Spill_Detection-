🛢️ Module 6: Deployment – Oil Spill Detection Web Application
📌 Module Objective

The objective of Module 6 is to deploy the trained oil spill segmentation model as a real-time, user-interactive web application.
This module demonstrates end-to-end deployment readiness, converting a trained deep learning model into a usable system for real-world monitoring.

🔁 Model Dependency (Important)

✔ This module uses the fine-tuned U-Net model saved in Module 5

Model format: Keras native format (.keras)

File used:

oil_spill_unet_finetuned.keras


The model was:

Trained

Fine-tuned

Validated

Saved in Module 5

Module 6 does NOT retrain the model, it only performs inference and visualization

This ensures:

Reproducibility

Separation of training and deployment

Industry-standard ML pipeline design

🏗️ System Architecture
User Upload Image
        ↓
Streamlit Web UI
        ↓
Preprocessing (Resize, Normalize)
        ↓
U-Net Model Inference (.keras)
        ↓
Postprocessing (Thresholding)
        ↓
Visualization + Alerts + Download

🧠 Technologies Used
Component	Technology
Frontend	Streamlit
Backend Inference	TensorFlow / Keras
Model	U-Net (SAR Image Segmentation)
Visualization	Matplotlib, OpenCV
Deployment	Streamlit Community Cloud
📂 Project Structure
module_6_deployment/
│
├── app.py                 # Streamlit web application
├── utils.py               # Inference & visualization utilities
├── oil_spill_unet_finetuned.keras   # Model from Module 5
├── requirements.txt       # Python dependencies
└── README.md              # Module documentation

⚙️ Application Features
🔹 1. Image Upload

Accepts satellite images in:

.png

.jpg

.jpeg

🔹 2. Real-Time Model Inference

Uses the fine-tuned U-Net model from Module 5

Performs pixel-wise oil spill segmentation

No retraining during deployment

🔹 3. Visualization Outputs

The app displays:

1️⃣ Original satellite image
2️⃣ Predicted segmentation mask (color-mapped)
3️⃣ Overlay of oil spill mask on the input image

🔹 4. Oil Spill Alert System

Calculates oil spill area percentage

Displays:

⚠️ Alert if oil spill detected

✅ Safe status otherwise

🔹 5. Download Prediction Results

Users can download:

Binary oil spill mask (.png)

Useful for:

Reports

Monitoring systems

Further analysis

🚀 How to Run the Application Locally
1️⃣ Install Dependencies
pip install -r requirements.txt

2️⃣ Run Streamlit App
streamlit run app.py

3️⃣ Open Browser
http://localhost:8501

🌐 Deployment

The application is deployed using Streamlit Community Cloud, making it accessible via a public URL.

✔ No server configuration required
✔ Free hosting
✔ Easy sharing for demos and evaluations

✅
🔚 Conclusion

Module 6 completes the end-to-end deep learning pipeline by transforming a trained segmentation model into a deployable, real-world application suitable for environmental monitoring, disaster management, and industrial use cases.
