import streamlit as st
from utils.localization import get_localized_strings

st.image("images/lung-cancer.png")
t = get_localized_strings()

st.title(t["info_page"]["title"])
st.markdown(t["info_page"]["intro"])

tabs = st.tabs([
    t["info_page"]["tabs"]["lung_cancer"],
    t["info_page"]["tabs"]["pneumonia"],
    t["info_page"]["tabs"]["tuberculosis"]
])

with tabs[0]:
    st.header(t["info_page"]["lung_cancer"]["what_is"]["header"])
    st.markdown(t["info_page"]["lung_cancer"]["what_is"]["content"])
    st.header(t["info_page"]["lung_cancer"]["statistics"]["header"])
    st.markdown(t["info_page"]["lung_cancer"]["statistics"]["content"])
    st.header(t["info_page"]["lung_cancer"]["symptoms"]["header"])
    st.markdown(t["info_page"]["lung_cancer"]["symptoms"]["content"])
    st.header(t["info_page"]["lung_cancer"]["causes_risk_factors"]["header"])
    st.markdown(t["info_page"]["lung_cancer"]["causes_risk_factors"]["content"])
    st.header(t["info_page"]["lung_cancer"]["diagnosis"]["header"])
    st.markdown(t["info_page"]["lung_cancer"]["diagnosis"]["content"])
    st.header(t["info_page"]["lung_cancer"]["treatment"]["header"])
    st.markdown(t["info_page"]["lung_cancer"]["treatment"]["content"])
    st.header(t["info_page"]["lung_cancer"]["prevention"]["header"])
    st.markdown(t["info_page"]["lung_cancer"]["prevention"]["content"])
    st.markdown(t["info_page"]["lung_cancer"]["conclusion"])
    st.markdown(f"### {t['info_page']['source_title']}")
    for source in t["info_page"]["lung_cancer"]["sources"]:
        st.markdown(f"- [{source['title']}]({source['url']})")

with tabs[1]:
    st.header(t["info_page"]["pneumonia"]["what_is"]["header"])
    st.markdown(t["info_page"]["pneumonia"]["what_is"]["content"])
    st.header(t["info_page"]["pneumonia"]["statistics"]["header"])
    st.markdown(t["info_page"]["pneumonia"]["statistics"]["content"])
    st.header(t["info_page"]["pneumonia"]["symptoms"]["header"])
    st.markdown(t["info_page"]["pneumonia"]["symptoms"]["content"])
    st.header(t["info_page"]["pneumonia"]["causes_risk_factors"]["header"])
    st.markdown(t["info_page"]["pneumonia"]["causes_risk_factors"]["content"])
    st.header(t["info_page"]["pneumonia"]["treatment"]["header"])
    st.markdown(t["info_page"]["pneumonia"]["treatment"]["content"])
    st.header(t["info_page"]["pneumonia"]["prevention"]["header"])
    st.markdown(t["info_page"]["pneumonia"]["prevention"]["content"])
    st.markdown(f"### {t['info_page']['source_title']}")
    for source in t["info_page"]["pneumonia"]["sources"]:
        st.markdown(f"- [{source['title']}]({source['url']})")

with tabs[2]:
    st.header(t["info_page"]["tuberculosis"]["what_is"]["header"])
    st.markdown(t["info_page"]["tuberculosis"]["what_is"]["content"])
    st.header(t["info_page"]["tuberculosis"]["statistics"]["header"])
    st.markdown(t["info_page"]["tuberculosis"]["statistics"]["content"])
    st.header(t["info_page"]["tuberculosis"]["symptoms"]["header"])
    st.markdown(t["info_page"]["tuberculosis"]["symptoms"]["content"])
    st.header(t["info_page"]["tuberculosis"]["causes_risk_factors"]["header"])
    st.markdown(t["info_page"]["tuberculosis"]["causes_risk_factors"]["content"])
    st.header(t["info_page"]["tuberculosis"]["treatment"]["header"])
    st.markdown(t["info_page"]["tuberculosis"]["treatment"]["content"])
    st.header(t["info_page"]["tuberculosis"]["prevention"]["header"])
    st.markdown(t["info_page"]["tuberculosis"]["prevention"]["content"])
    st.markdown(f"### {t['info_page']['source_title']}")
    for source in t["info_page"]["tuberculosis"]["sources"]:
        st.markdown(f"- [{source['title']}]({source['url']})")