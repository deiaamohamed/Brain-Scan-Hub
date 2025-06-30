# brain_filter/setup.py

import torch
import torch.nn as nn
from torchvision import models
from Brainapp.ML.config import DEVICE

# Define the autoencoder
class Autoencoder(nn.Module):
    def __init__(self):
        super(Autoencoder, self).__init__()
        self.encoder = nn.Sequential(
            nn.Conv2d(3, 32, 3, stride=2, padding=1), nn.ReLU(),
            nn.Conv2d(32, 64, 3, stride=2, padding=1), nn.ReLU(),
            nn.Conv2d(64, 128, 3, stride=2, padding=1), nn.ReLU()
        )
        self.decoder = nn.Sequential(
            nn.ConvTranspose2d(128, 64, 3, stride=2, padding=1, output_padding=1), nn.ReLU(),
            nn.ConvTranspose2d(64, 32, 3, stride=2, padding=1, output_padding=1), nn.ReLU(),
            nn.ConvTranspose2d(32, 3, 3, stride=2, padding=1, output_padding=1), nn.Tanh()
        )

    def forward(self, x):
        return self.decoder(self.encoder(x))

# Download VGG for generating features
def get_feature_extractor():
    vgg = models.vgg16(pretrained=True).features[:8].eval().to(DEVICE)
    for p in vgg.parameters():
        p.requires_grad = False
    return vgg

# Download the model
def load_model(model_path):
    model = Autoencoder().to(DEVICE)
    model.load_state_dict(torch.load(model_path, map_location=DEVICE))
    model.eval()
    return model
