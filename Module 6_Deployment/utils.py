import cv2
import numpy as np

IMG_SIZE = 256

def preprocess_image(image):
    img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    img = img.astype(np.float32) / 255.0
    img = img[..., np.newaxis]
    img = np.expand_dims(img, axis=0)
    return img

def predict_mask(model, image, threshold=0.5):
    img_input = preprocess_image(image)
    pred = model.predict(img_input, verbose=0)[0, ..., 0]
    binary_mask = (pred > threshold).astype(np.uint8)
    return pred, binary_mask

def overlay_mask(image, mask):
    image = cv2.resize(np.array(image), (IMG_SIZE, IMG_SIZE))
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    overlay = image.copy()
    overlay[mask == 1] = [255, 0, 0]  # Red oil spill

    blended = cv2.addWeighted(image, 0.7, overlay, 0.3, 0)
    return cv2.cvtColor(blended, cv2.COLOR_BGR2RGB)
