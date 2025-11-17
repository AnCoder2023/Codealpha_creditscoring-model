import streamlit as st
import joblib
import numpy as np

st.title("Iris Flower Classification 🌸")
st.write("Predict the Iris flower species using a trained ML model.")

# Load the trained model
model = joblib.load("iris_model.pkl")

# Input sliders
sepal_length = st.slider("Sepal Length (cm)", 0.0, 10.0, 5.0)
sepal_width = st.slider("Sepal Width (cm)", 0.0, 10.0, 3.0)
petal_length = st.slider("Petal Length (cm)", 0.0, 10.0, 1.0)
petal_width = st.slider("Petal Width (cm)", 0.0, 10.0, 0.5)

# Predict
if st.button("Predict"):
    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(features)[0]

    species = ["Setosa", "Versicolor", "Virginica"]
    st.success(f"Predicted Species: **{species[prediction]}**")
