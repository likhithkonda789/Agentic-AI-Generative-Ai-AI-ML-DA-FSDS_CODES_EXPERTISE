import streamlit as st
import joblib
import pandas as pd
import numpy as np
import os

st.set_page_config(page_title="Customer Churn Prediction")

# Load the pre-trained model and encoders
model_path = r"C:\Users\LIKHITH\OneDrive\Desktop\Data science\Jan\ML capstone projects\churn modeling testing pending\best_model.pkl"
scaler_path = r"C:\Users\LIKHITH\OneDrive\Desktop\Data science\Jan\ML capstone projects\churn modeling testing pending\scaler.joblib"
encoder_path = r"C:\Users\LIKHITH\OneDrive\Desktop\Data science\Jan\ML capstone projects\churn modeling testing pending\encoder.joblib"

# Check if required files exist
if not os.path.exists(model_path) or not os.path.exists(scaler_path) or not os.path.exists(encoder_path):
    st.error("Required files not found. Please ensure 'best_model.pkl', 'scaler.joblib', and 'encoder.joblib' are present.")
else:
    # Load the model, scaler, and encoder
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    encoder = joblib.load(encoder_path)

    # Streamlit app
    st.title("Customer Churn Prediction")

    # Input fields for numerical features
    st.header('Customer Data Input')
    numerical_features = ['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'EstimatedSalary']
    categorical_features = ['Geography', 'Gender']

    # Create input fields for each feature
    input_data = {}

    for feature in numerical_features:
        if feature in ['HasCrCard', 'IsActiveMember']:
            input_data[feature] = st.selectbox(f"Enter {feature}", options=["Yes", "No"])
        else:
            input_data[feature] = st.number_input(
                f"Enter {feature}", value=0.0 if feature == 'Balance' else 1.0, step=1.0
            )

    for feature in categorical_features:
        input_data[feature] = st.selectbox(f"Enter {feature}", options=encoder.categories_[categorical_features.index(feature)])

    # Convert categorical inputs to encoded format
    categorical_data = pd.DataFrame([{k: input_data[k] for k in categorical_features}])
    encoded_data = encoder.transform(categorical_data).toarray()

    # Convert numerical inputs to scaled format
    numerical_data = pd.DataFrame([{k: input_data[k] for k in numerical_features}])
    numerical_data['HasCrCard'] = numerical_data['HasCrCard'].apply(lambda x: 1 if x == "Yes" else 0)
    numerical_data['IsActiveMember'] = numerical_data['IsActiveMember'].apply(lambda x: 1 if x == "Yes" else 0)
    scaled_data = scaler.transform(numerical_data)

    # Combine numerical and categorical data
    final_input = np.hstack([scaled_data, encoded_data])

    # Predict churn
    if st.button("Predict"):
        prediction = model.predict(final_input)
        prediction_text = "Yes" if prediction[0] == 1 else "No"
        st.success(f"Churn Prediction: {prediction_text}")

    # Optionally display input data for verification
    st.write("### Input Data")
    st.write(numerical_data.join(categorical_data))
