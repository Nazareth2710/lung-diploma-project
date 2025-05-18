import pickle
import streamlit as st
import torch
from torchvision import transforms

@st.cache_resource
def load_model(model_path="models/bnb_model.pkl"):
    with open(model_path, "rb") as file:
        model = pickle.load(file)
    return model

@st.cache_resource
def image_load_model(CLASS_NAMES, MODEL_PATH):
    from torchvision.models import resnet18
    model = resnet18(pretrained=False)
    model.fc = torch.nn.Linear(model.fc.in_features, len(CLASS_NAMES))
    model.load_state_dict(torch.load(MODEL_PATH, map_location='cpu'))
    model.eval()
    return model

def get_transform():
    return transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.Grayscale(num_output_channels=3),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225])
    ])
