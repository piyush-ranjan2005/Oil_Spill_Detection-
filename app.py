import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image

st.title("Oil Spill Detection – Prototype")

model = tf.keras.models.load_model("oil_spill_model.keras")

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).resize((224, 224))
    img_array = np.array(image) / 255.0

    prediction = model.predict(img_array.reshape(1, 224, 224, 3))

    st.image(image, caption="Uploaded Image", use_column_width=True)
    st.write("Prediction Score:", prediction[0][0])
