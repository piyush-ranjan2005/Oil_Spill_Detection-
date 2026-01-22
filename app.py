import streamlit as st
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from pathlib import Path
from PIL import Image

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
# Load Model (SAFE + CACHED)
# -------------------------
@st.cache_resource
def load_trained_model():
    model_path = Path("models/unet_oil_spill_model.h5")
    if not model_path.exists():
        st.error("❌ Model file not found in 'models/' folder")
        st.stop()
    return tf.keras.models.load_model(model_path, compile=False)

model = load_trained_model()

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
    try:
        # Read image safely with PIL (NO OpenCV)
        image = Image.open(uploaded_file).convert("L")
        image = np.array(image)
    except Exception:
        st.error("❌ Unable to read the uploaded image")
        st.stop()

    st.subheader("Original Image")
    st.image(image, clamp=True)

    # -------------------------
    # Preprocessing
    # -------------------------
    IMG_SIZE = 256

    image_resized = Image.fromarray(image).resize(
        (IMG_SIZE, IMG_SIZE),
        resample=Image.BILINEAR
    )
    image_resized = np.array(image_resized, dtype=np.float32) / 255.0

    # Model input shape: (1, 256, 256, 1)
    image_input = image_resized[np.newaxis, ..., np.newaxis]

    # -------------------------
    # Prediction
    # -------------------------
    with st.spinner("🔍 Detecting oil spill regions..."):
        prediction = model.predict(image_input, verbose=0)

    mask = (prediction[0, :, :, 0] > 0.5).astype(np.uint8)

    # -------------------------
    # Display Results
    # -------------------------
    st.subheader("Predicted Oil Spill Mask")
    st.image(mask * 255, clamp=True)

    st.subheader("Overlay Visualization")
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.imshow(image_resized, cmap="gray")
    ax.imshow(mask, cmap="jet", alpha=0.5)
    ax.axis("off")
    st.pyplot(fig)


