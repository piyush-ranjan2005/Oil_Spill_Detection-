import streamlit as st
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import io

from utils import predict_mask, overlay_mask

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Oil Spill Detection",
    layout="wide"
)

st.title("🛢️ Oil Spill Detection using Deep Learning")
st.markdown("Upload a satellite image to detect oil spills in real-time.")

# -------------------------------
# Load Model (Cached)
# -------------------------------
@st.cache_resource
def load_trained_model():
    model = tf.keras.models.load_model(
        "oil_spill_unet_finetuned.keras",
        compile=False
    )
    return model

model = load_trained_model()

# -------------------------------
# File Upload
# -------------------------------
uploaded_file = st.file_uploader(
    "Upload Satellite Image",
    type=["jpg", "jpeg", "png"]
)

# -------------------------------
# Prediction Pipeline
# -------------------------------
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")

    st.subheader("Prediction Results")

    col1, col2, col3 = st.columns(3)

    # Inference
    prob_mask, bin_mask = predict_mask(model, image)
    overlay = overlay_mask(image, bin_mask)

    # -------------------------------
    # Visualization
    # -------------------------------
    with col1:
        st.markdown("**Original Image**")
        st.image(image, use_container_width=True)

    with col2:
        st.markdown("**Predicted Mask**")
        plt.imshow(prob_mask, cmap="jet")
        plt.axis("off")
        st.pyplot(plt.gcf())
        plt.clf()

    with col3:
        st.markdown("**Overlay Result**")
        st.image(overlay, use_container_width=True)

    # -------------------------------
    # Alert Logic
    # -------------------------------
    spill_percentage = (bin_mask.sum() / bin_mask.size) * 100

    if spill_percentage > 1:
        st.error(f"⚠️ Oil Spill Detected ({spill_percentage:.2f}% area)")
    else:
        st.success("✅ No Significant Oil Spill Detected")

    # -------------------------------
    # Download Predicted Mask
    # -------------------------------
    mask_img = Image.fromarray((bin_mask * 255).astype(np.uint8))

    buffer = io.BytesIO()
    mask_img.save(buffer, format="PNG")
    byte_data = buffer.getvalue()

    st.download_button(
        label="📥 Download Predicted Mask",
        data=byte_data,
        file_name="oil_spill_mask.png",
        mime="image/png"
    )

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.markdown(
    "Built using U-Net, TensorFlow, and Streamlit • Module 6 Deployment"
)