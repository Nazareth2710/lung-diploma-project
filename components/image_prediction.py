import streamlit as st
from utils.localization import get_localized_strings
from utils.prediction import image_load_model, get_transform

import torch
from PIL import Image
import numpy as np

CLASS_NAMES = ['NORMAL', 'PNEUMONIA', 'UNKNOWN', 'TUBERCULOSIS']
MODEL_PATH = 'models/resnet18_model.pt'

t = get_localized_strings()
st.image("images/lung-cancer-3.png")

st.title(t["image_prediction"]["title"])
st.write(t["image_prediction"]["description"])

model = image_load_model(CLASS_NAMES, MODEL_PATH)
uploaded_file = st.file_uploader("Оберіть зображення рентгену", type=["jpg", "jpeg", "png", "bmp"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Завантажене зображення", use_container_width=True)

    transform = get_transform()
    img_tensor = transform(image).unsqueeze(0)

    with torch.no_grad():
        outputs = model(img_tensor)
        probs = torch.softmax(outputs, dim=1).cpu().numpy()[0]
        pred_idx = np.argmax(probs)
        pred_class = CLASS_NAMES[pred_idx]
        prob_str = ", ".join([f"{cls}: {prob*100:.1f}%" for cls, prob in zip(CLASS_NAMES, probs)])

    st.markdown(f"**Результат:** {pred_class}")
    st.markdown(f"**Впевненість моделі:** {prob_str}")
else:
    st.info("Для аналізу, будь ласка, завантажте рентгенівське зображення.")