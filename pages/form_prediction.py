import streamlit as st
import numpy as np
from utils.localization import get_localized_strings
from utils.prediction import load_model

HIGH_RISK_THRESHOLD = 65
MEDIUM_RISK_THRESHOLD = 30

t = get_localized_strings()["form_prediction"]
st.image("images/lung-cancer-5.png")

st.title(t["title"])
yes_no = [t["yes"], t["no"]]

binary_questions_keys = [
    "smoking", "yellow_fingers", "anxiety", "peer_pressure",
    "chronic_disease", "fatigue", "allergy", "wheezing",
    "alcohol_consuming", "coughing", "shortness_of_breath",
    "swallowing_difficulty", "chest_pain"
]


available_models = {
    "Naive Bayes": "models/bnb_model.pkl",
    "K-Nearest Neighbors": "models/knn_model.pkl",
    "XGBoost": "models/xgb_model.pkl"
}

with st.form("prediction_form"):
    model_choice = st.selectbox("🔍 Оберіть модель прогнозування:", list(available_models.keys()))
    model_path = available_models[model_choice]
    model = load_model(model_path)

    gender = st.selectbox(t["gender"], [t["male"], t["female"]])
    age = st.slider(t["age"], 1, 120, 18)

    col1, col2 = st.columns(2)
    answers = {}

    half = len(binary_questions_keys) // 2
    for i, key in enumerate(binary_questions_keys):
        col = col1 if i < half else col2
        with col:
            answers[key] = st.radio(
                t["questions"][key],
                yes_no,
                index=None,
                key=key
            )

    submit = st.form_submit_button(t["submit"])

if submit:
    if any(ans is None for ans in answers.values()):
        st.warning(t["warning_unanswered"], icon=":material/warning:")
    else:
        def to_binary(val): return 1 if val == t["yes"] else 0

        gender_val = 1 if gender == t["male"] else 0
        input_data = np.array([[
            gender_val,
            age,
            *[to_binary(answers[key]) for key in binary_questions_keys]
        ]])

        probabilities = model.predict_proba(input_data)[0]
        risk_percent = round(probabilities[1] * 100, 2)

        st.subheader(t["results"]["title"])
        if risk_percent >= HIGH_RISK_THRESHOLD:
            st.error(t["results"]["high"].format(risk=risk_percent), icon=":material/priority_high:")
        elif risk_percent >= MEDIUM_RISK_THRESHOLD:
            st.warning(t["results"]["medium"].format(risk=risk_percent), icon=":material/warning:")
        else:
            st.success(t["results"]["low"].format(risk=risk_percent), icon=":material/thumb_up:")