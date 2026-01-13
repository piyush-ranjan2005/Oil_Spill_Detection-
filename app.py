import streamlit as st
from model import AttentionUNet
import torch
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import cv2
import pathlib

st.set_page_config(
    page_title="Oil Spill Segmentation",
    layout="centered"
)

st.title("Oil Spill Detection")
st.write("Upload a SAR image to detect oil spill regions.")

@st.cache_resource
def load_model():
    model = AttentionUNet(in_channels=1, out_channels=1)
    model.load_state_dict(torch.load("attention_unet.pth", map_location=torch.device('cpu')))
    model.eval()
    return model

model=load_model()

def preprocess_image(image):
    image=image.convert("L")  # Convert to grayscale
    image=image.resize((256,256))
    image_np=np.array(image)/255.0
    image_np=cv2.medianBlur(
        (image_np*255).astype(np.uint8),3
    )/255.0

    img_tensor=torch.tensor(
        image_np,dtype=torch.float32
    ).unsqueeze(0).unsqueeze(0)  
    
    return img_tensor

def predict_mask(model,img_tensor,threshold=0.65):
    with torch.no_grad():
        output=model(img_tensor)
        prob=torch.sigmoid(output)
        mask=(prob>threshold).float()
    return mask.squeeze().numpy()

def post_process(mask):
    kernel=np.ones((3,3),np.uint8)
    mask=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
    mask=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
    return mask

uploaded_file=st.file_uploader(
    "Upload SAR Image",
    type=["png","jpg","jpeg","tif","tiff"]
)

if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.subheader("Original Image")
    st.image(image,use_container_width=True)

    input_tensor=preprocess_image(image)
    pred_mask=predict_mask(model,input_tensor)
    refined_mask=post_process(pred_mask)

    fig,ax=plt.subplots(1,3,figsize=(14,4))
    ax[0].imshow(image.convert("L"),cmap="gray")
    ax[0].set_title("Input Image")
    ax[0].axis("off")

    ax[1].imshow(pred_mask,cmap="gray")
    ax[1].set_title("Predicted Mask")
    ax[1].axis("off")

    ax[2].imshow(image.convert("L"),cmap="gray")
    ax[2].imshow(refined_mask,cmap="gray",alpha=0.5)
    ax[2].set_title("Refined Mask")
    ax[2].axis("off")

    st.pyplot(fig)

    if(refined_mask.sum()>0.5):
        st.warning("Potential Oil Spill Detected!")

    else:
        st.success("No Oil Spill Detected.")

    st.download_button(
        "Download Predicted Mask",
        data=(refined_mask*255).astype(np.uint8).tobytes(),
        file_name="predicted_mask.png",
        mime="image/png"
    )



