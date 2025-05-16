import streamlit as st
from utils.theming import render_theme_toggle
from utils.localization import set_language, get_localized_strings

st.set_page_config(
    page_title="Lung Disease App",
    page_icon="images/favicon.ico",
    initial_sidebar_state="expanded"
)

st.logo("images/lung_cancer_logo_full.png", icon_image='images/lung_cancer_logo_icon.png', size='large')
t = get_localized_strings()

pages = {
    "": [
        st.Page("components/home.py", title=t["pages"]["home"], icon=":material/home:"),
        st.Page("components/info_page.py", title=t["pages"]["info"], icon=":material/pulmonology:"),
        st.Page("components/image_prediction.py", title=t["pages"]["image_prediction"], icon=":material/respiratory_rate:"),
        st.Page("components/form_prediction.py", title=t["pages"]["prediction"], icon=":material/blood_pressure:"),
        st.Page("components/about_us.py", title=t["pages"]["about"], icon=":material/info:")
    ]
}
render_theme_toggle()
set_language()
st.sidebar.caption("Made by Umantsiv N., 2025")

pg = st.navigation(pages)
pg.run()
