[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-%23FE4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)](https://pytorch.org/)
[![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)](https://matplotlib.org/)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)

# Lung Diseases App — Оцінка ризику раку легень

**Lung Diseases App** — це веб-додаток на базі Streamlit, який дозволяє користувачам пройти коротке опитування для попередньої оцінки ризику розвитку раку легень та проаналізувати рентгенівськи зображення для виявлення пневмонії та туберкульозу. Проєкт розроблено у рамках дипломної роботи "Розробка системи ранньої діагностики захворювання легень з використанням машинного навчання".

---

## 🔍 Основні можливості

- 🧠 Прогнозування з використанням кількох моделей (Naive Bayes Bernoulli, XGBoost, Logistic Regression).
- 🧩 Аналіз рентгенівських знімків за допомоги ResNet-18
- 🌐 Підтримка української та англійської мов.
- 🌓 Автоматична або ручна зміна теми (світла/темна).
- 🩺 Інформаційна сторінка про рак легень.
- 📱 Інтерфейс, адаптований для мобільних пристроїв.

---
## 🔧 Як запустити на локальному комп'ютері

> Потрібно мати встановлений **Python 3.12+** та **pip**

1. Клонуйте репозиторій:
```bash
git clone https://github.com/Nazareth2710/lung-diploma-project.git
cd lung-diploma-project
```

2. Встановіть залежності:
```bash
pip install -r requirements.txt
```

3. Запустіть додаток:
```bash
streamlit run main.py
```

4. Відкрийте у браузері:
```bash
http://localhost:8501
```

## 📦 Як запустити на сервері з Docker

1. Побудуйте Docker-образ:
```bash
docker build -t lung-diploma-project .
```

2. Запустіть контейнер:
```bash
docker run -p 8501:8501 lung-diploma-project
```

