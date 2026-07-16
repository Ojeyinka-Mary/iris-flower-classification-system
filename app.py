import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("iris_model.joblib")

st.title("Iris Flower Classification System")

st.write("Enter flower measurements below:")

sepal_length = st.number_input("Sepal Length", min_value=0.0)
sepal_width = st.number_input("Sepal Width", min_value=0.0)
petal_length = st.number_input("Petal Length", min_value=0.0)
petal_width = st.number_input("Petal Width", min_value=0.0)

if st.button("Predict"):

    prediction = model.predict([[
        sepal_length,
        sepal_width,
        petal_length,
        petal_width
    ]])

    classes = [
        "Setosa",
        "Versicolor",
        "Virginica"
    ]

    st.success(
        f"Predicted Flower Species: {classes[prediction[0]]}"
    )