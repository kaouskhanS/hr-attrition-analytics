import streamlit as st
import requests

st.title("HR Attrition Prediction")

age = st.slider("Age", 18, 60)
income = st.slider("Monthly Income", 2000, 20000)
overtime = st.selectbox("OverTime", [0,1])
satisfaction = st.slider("Job Satisfaction", 1, 4)
years = st.slider("Years at Company", 0, 20)

if st.button("Predict"):
    response = requests.post("http://localhost:8000/predict", json={
        "Age": age,
        "MonthlyIncome": income,
        "OverTime": overtime,
        "JobSatisfaction": satisfaction,
        "YearsAtCompany": years
    })
    st.write(response.json())
