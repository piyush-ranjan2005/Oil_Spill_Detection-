import streamlit as st
import torch
from torchvision import transforms
from PIL import Image
import io
import os

# Define the device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Define the model architecture (ResNet18 with 2 output classes)
import torch.nn as nn
import torchvision.models as models

class OilSpillClassifier(nn.Module):
    def __init__(self, num_classes=2):
        super(OilSpillClassifier, self).__init__()
        # Load a pre-trained ResNet18 model
        self.model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
        # Modify the final classification layer
        num_ftrs = self.model.fc.in_features
        self.model.fc = nn.Linear(num_ftrs, num_classes)

    def forward(self, x):
        return self.model(x)

# Instantiate the model
model = OilSpillClassifier(num_classes=2).to(device)

# Load the saved model weights
model_path = 'oil_spill_model2.pth' # Assuming the model was saved with this name
if os.path.exists(model_path):
    # Load state_dict into the internal ResNet model
    model.model.load_state_dict(torch.load(model_path, map_location=device))
    model.eval()
    st.success("Model loaded successfully!")
else:
    st.error(f"Model file not found at {model_path}. Please ensure the model is trained and saved correctly.")
    st.stop() # Stop Streamlit app if model not found

# Define the image transformations
image_size = 224
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(image_size),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# Streamlit App Title
st.title("Oil Spill Detection from SAR Images")
st.write("Upload a Synthetic Aperture Radar (SAR) image to detect oil spills.")

# File Uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption='Uploaded Image', use_column_width=True)
    st.write("")

    # Preprocess the image
    input_tensor = transform(image).unsqueeze(0).to(device) # Add batch dimension and move to device

    # Make prediction
    with torch.no_grad():
        outputs = model(input_tensor)
        probabilities = torch.nn.functional.softmax(outputs, dim=1)
        _, predicted_class = torch.max(outputs, 1)

    # Display prediction
    class_names = {0: "No Oil Spill", 1: "Oil Spill"}
    predicted_label = class_names[predicted_class.item()]
    confidence = probabilities[0][predicted_class.item()].item()

    st.subheader(f"Prediction: {predicted_label}")
    st.write(f"Confidence: {confidence:.2f}")

    if predicted_class.item() == 1:
        st.error("Potential Oil Spill Detected!")
    else:
        st.success("No Oil Spill Detected.")

else:
    st.info("Please upload an image to get a prediction.")
