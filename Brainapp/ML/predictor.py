# brain_filter/predictor.py

import torch
from PIL import Image
from torchvision import transforms
import os
from Brainapp.ML.setup import load_model, get_feature_extractor
from Brainapp.ML.config import MODEL_PATH, DEVICE, THRESHOLD

# Download the model and VGG once
model = load_model(MODEL_PATH)
vgg = get_feature_extractor()
loss_fn = torch.nn.MSELoss()

# Image Processing
transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor(),
    transforms.Normalize([0.5]*3, [0.5]*3)
])

# Get features from VGG
def get_features(img):
    return vgg(img)

# Predict whether or not the image is a brain or not
def is_brain_image(image):
    img = Image.open(image).convert("RGB")
    img_tensor = transform(img).unsqueeze(0).to(DEVICE)

    with torch.no_grad():
        output = model(img_tensor)
        loss = loss_fn(get_features(output), get_features(img_tensor)).item()

    is_brain = loss <= THRESHOLD
    return is_brain
