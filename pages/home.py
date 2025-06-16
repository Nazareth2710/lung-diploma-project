import streamlit as st
from utils.localization import get_localized_strings

t = get_localized_strings()
st.image("images/lung-cancer-2.png")

st.title(t["home_page"]["title"])
st.write(t["home_page"]["description"])

col1, col2 = st.columns(2)

with col1:
    if st.button(t["home_page"]["go_to_image"], use_container_width=True):
        st.switch_page("pages/image_prediction.py")

with col2:
    if st.button(t["home_page"]["go_to_form"], use_container_width=True):
        st.switch_page("pages/form_prediction.py")
