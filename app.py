import streamlit as st
import torch
import cv2
import numpy as np
import segmentation_models_pytorch as smp

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

model = smp.Unet(
    encoder_name="resnet34",
    encoder_weights=None,
    in_channels=3,
    classes=1
)

model.load_state_dict(torch.load("oil_spill_unet.pth", map_location=DEVICE))
model.to(DEVICE)
model.eval()

st.title("Oil Spill Detection System")

uploaded_file = st.file_uploader(
    "Upload a satellite image",
    type=["jpg", "png", "jpeg"]
)

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    image = cv2.resize(image, (256, 256))

    img_tensor = torch.tensor(image).permute(2, 0, 1)
    img_tensor = img_tensor.unsqueeze(0).float() / 255.0
    img_tensor = img_tensor.to(DEVICE)

    with torch.no_grad():
        output = model(img_tensor)
        output = torch.sigmoid(output)
        mask = (output.squeeze().cpu().numpy() > 0.5).astype(np.uint8)

    st.subheader("Input Image")
    st.image(image)

    st.subheader("Predicted Oil Spill Mask")
    st.image(mask * 255, clamp=True)
