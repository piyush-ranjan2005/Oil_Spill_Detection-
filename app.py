import streamlit as st
import torch
import numpy as np
import cv2
from PIL import Image
from model import UNet

TARGET_SIZE = (256, 256)

# ---------------------------
# Preprocessing (SAME AS TRAINING)
# ---------------------------
def preprocess_sar_image(image, target_size=(256,256)):

    if image.ndim == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    img = cv2.resize(image, target_size, interpolation=cv2.INTER_LINEAR)

    if img.dtype != np.uint8:
        img = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

    img = cv2.medianBlur(img, 3)

    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    img = clahe.apply(img)

    img = img.astype(np.float32) / 255.0

    return img


# ---------------------------
# Load Model (Cached)
# ---------------------------
@st.cache_resource
def load_model():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = UNet(in_channels=1, num_classes=2)
    model.load_state_dict(
        torch.load("sar_unet_model.pth", map_location=device)
    )
    model.to(device)
    model.eval()
    return model, device


model, device = load_model()

# ---------------------------
# Streamlit UI
# ---------------------------
st.set_page_config(layout="wide")
st.title("🛰 SAR Image Segmentation using UNet")

uploaded_file = st.file_uploader(
    "Upload SAR Image", type=["png", "jpg", "jpeg"]
)

if uploaded_file:

    # Read Image
    image = Image.open(uploaded_file)
    image_np = np.array(image)

    # Preprocess
    proc_img = preprocess_sar_image(image_np)
    input_tensor = torch.tensor(proc_img).unsqueeze(0).unsqueeze(0).to(device)

    # Inference
    with torch.no_grad():
        output = model(input_tensor)
        pred = torch.softmax(output, dim=1)
        mask = pred[0, 1].cpu().numpy()   # class-1

    # Threshold
    binary_mask = (mask > 0.5).astype(np.uint8)

    # Display
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Original Image")
        st.image(image_np, clamp=True)

    with col2:
        st.subheader("Preprocessed Image")
        st.image(proc_img, clamp=True)

    with col3:
        st.subheader("Predicted Mask")
        st.image(binary_mask * 255, clamp=True)
