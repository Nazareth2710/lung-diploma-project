import streamlit as st
from utils.localization import get_localized_strings

t = get_localized_strings()
st.image("images/lung-cancer-5.png")

st.title(t["image_prediction"]["title"])
st.write(t["image_prediction"]["description"])