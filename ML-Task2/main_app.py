import streamlit as st
import numpy as np
import pickle

# Load the trained model
model = pickle.load(open('rf_model.pkl', 'rb'))

st.title('Student Posttest Score Predictor')

# Input features from user
n_student = st.number_input('Number of students in class', min_value=0)
pretest = st.number_input('Pretest score', min_value=0, max_value=100)

# Make prediction
if st.button('Predict'):
    prediction = model.predict(np.array([[n_student, pretest, ...]]))  # Add other features accordingly
    st.write(f"Predicted Posttest Score: {prediction}")
