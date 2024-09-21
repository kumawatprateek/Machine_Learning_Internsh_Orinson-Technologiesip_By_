import streamlit as st
import numpy as np
import pickle

# Load the trained model
with open('rf_model', 'rb') as f:
    model = pickle.load(f)

st.title('Student Score Predictor')

# Input features from user
n_student = st.number_input('Number of students in class', min_value=0)
pretest = st.number_input('Pretest score', min_value=0, max_value=100)

# Add a slider for the new input feature
slider_input1 = st.select_slider('Select a category', options=['Urban', 'Rural', 'Suburban'])
s_mapping1 = {'Urban': [0,1], 'Rural': [0,0], 'Suburban': [1,0]}
s_value1 = s_mapping1[slider_input1]

# Add a slider for the new input feature
slider_input2 = st.select_slider('Select a category', options=['Non-public', 'Public'])
s_mapping2 = {'Non-public': 0, 'Public': 1}
s_value2 = s_mapping2[slider_input2]

# Add a slider for the new input feature
slider_input3 = st.select_slider('Select a category', options=['Standard', 'Experimental'])
s_mapping3 = {'Standard': 1, 'Experimental': 0}
s_value3 = s_mapping3[slider_input3]

# Add a slider for the new input feature
slider_input4 = st.select_slider('Select a category', options=['Male', 'Female'])
s_mapping4 = {'Male': 1, 'Female': 0}
s_value4 = s_mapping4[slider_input4]

# Add a slider for the new input feature
slider_input5 = st.select_slider('Select a category', options=['Qualifies for reduced/free lunch', 'Does not qualify'])
s_mapping5 = {'Qualifies for reduced/free lunch': 1, 'Does not qualify': 0}
s_value5 = s_mapping5[slider_input5]


# Check input data shape
st.write(f"Input features: Number of students = {n_student}, Pretest score = {pretest}")

# Make prediction
if st.button('Predict'):
    # Ensure the input matches the expected shape (adjust depending on your model's training data)
    add_data=[n_student, pretest]+s_value1+[s_value2,s_value3,s_value4,s_value5]
    print(add_data)
    new_data = np.array([add_data])  # Add more features accordingly

    st.write(f"Input data shape: {new_data.shape}")

    try:
        prediction = model.predict(new_data)
        st.write(f"Predicted Posttest Score: {prediction[0]}")
    except Exception as e:
        st.write(f"Error making prediction: {e}")
