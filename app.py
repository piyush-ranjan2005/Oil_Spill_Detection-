import streamlit as st
import numpy as np
import cv2
import tensorflow as tf
import matplotlib.pyplot as plt
from pathlib import Path

# -------------------------
# Streamlit Page Config
# -------------------------
st.set_page_config(
    page_title="Oil Spill Detection",
    layout="centered"
)

st.title("🛢️ Oil Spill Detection using Satellite Images")
st.write("Upload a satellite image to detect oil spill regions in real-time.")

# -------------------------
# Load Model (SAFE)
# -------------------------
@st.cache_resource
def load_model():
    model_path = Path("models/unet_oil_spill_model.h5")
    if not model_path.exists():
        st.error("❌ Model file not found in 'models/' folder")
        st.stop()
    return tf.keras.models.load_model(model_path, compile=False)

model = load_model()

# -------------------------
# Image Upload
# -------------------------
uploaded_file = st.file_uploader(
    "Upload Satellite Image (PNG / JPG)",
    type=["png", "jpg", "jpeg"]
)

# -------------------------
# Inference Pipeline
# -------------------------
if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_GRAYSCALE)

    if image is None:
        st.error("❌ Invalid image file")
        st.stop()

    st.subheader("Original Image")
    st.image(image, clamp=True)

    # Preprocessing
    IMG_SIZE = 256
    image_resized = cv2.resize(image, (IMG_SIZE, IMG_SIZE))
    image_norm = image_resized.astype(np.float32) / 255.0
    image_input = image_norm[np.newaxis, ..., np.newaxis]

    # Prediction
    prediction = model.predict(image_input)
    mask = (prediction[0, :, :, 0] > 0.5).astype(np.uint8)

    # Display Mask
    st.subheader("Predicted Oil Spill Mask")
    st.image(mask * 255, clamp=True)

    # Overlay Visualization
    st.subheader("Overlay Visualization")
    fig, ax = plt.subplots()
    ax.imshow(image_resized, cmap="gray")
    ax.imshow(mask, cmap="jet", alpha=0.5)
    ax.axis("off")
    st.pyplot(fig)
