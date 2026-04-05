import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model
model = joblib.load(r"C:\Users\LIKHITH\OneDrive\Desktop\Data science\Jan\ML capstone projects\customer churn\final_gb_classifier.pkl")

# Function to preprocess input data
def preprocess_input(data):
    # Convert input data to DataFrame
    df = pd.DataFrame(data, index=[0])
    
    # Convert categorical variables to numeric
    df['InternetService'] = df['InternetService'].map({'DSL': 0, 'Fiber optic': 1, 'No': 2})
    df['Contract'] = df['Contract'].map({'Month-to-month': 0, 'One year': 1, 'Two year': 2})
    df['PaymentMethod'] = df['PaymentMethod'].map({'Electronic check': 0, 'Mailed check': 1, 'Bank transfer (automatic)': 2, 'Credit card (automatic)': 3})
    
    # Return preprocessed DataFrame
    return df

# Streamlit UI
st.title("Customer Churn Prediction")

# Collect user inputs
gender = st.radio("Gender", [0, 1])
senior_citizen = st.radio("Senior Citizen", [0, 1])
partner = st.radio("Partner", [0, 1])
dependents = st.radio("Dependents", [0, 1])
phone_service = st.radio("Phone Service", [0, 1])
multiple_lines = st.radio("Multiple Lines", [0, 1])
internet_service = st.selectbox("Internet Service", ['DSL', 'Fiber optic', 'No'])
online_security = st.radio("Online Security", [0, 1, 2])
online_backup = st.radio("Online Backup", [0, 1, 2])
device_protection = st.radio("Device Protection", [0, 1, 2])
tech_support = st.radio("Tech Support", [0, 1, 2])
streaming_tv = st.radio("Streaming TV", [0, 1])
streaming_movies = st.radio("Streaming Movies", [0, 1])
contract = st.selectbox("Contract", ['Month-to-month', 'One year', 'Two year'])
paperless_billing = st.radio("Paperless Billing", [0, 1])
payment_method = st.selectbox("Payment Method", ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'])
monthly_charges = st.number_input("Monthly Charges", value=0.0)
total_charges = st.number_input("Total Charges", value=0.0)
tenure_group = st.number_input("Tenure Group", value=0)

# Make prediction
if st.button("Predict"):
    # Create dictionary from user inputs
    user_data = {
        'gender': gender,
        'SeniorCitizen': senior_citizen,
        'Partner': partner,
        'Dependents': dependents,
        'PhoneService': phone_service,
        'MultipleLines': multiple_lines,
        'InternetService': internet_service,
        'OnlineSecurity': online_security,
        'OnlineBackup': online_backup,
        'DeviceProtection': device_protection,
        'TechSupport': tech_support,
        'StreamingTV': streaming_tv,
        'StreamingMovies': streaming_movies,
        'Contract': contract,
        'PaperlessBilling': paperless_billing,
        'PaymentMethod': payment_method,
        'MonthlyCharges': monthly_charges,
        'TotalCharges': total_charges,
        'tenure_group': tenure_group
    }
    
    # Preprocess input data
    processed_data = preprocess_input(user_data)
    
    # Make prediction
    prediction = model.predict(processed_data)
    
    # Display prediction result
    if prediction[0] == 1:
        st.write("The customer is likely to churn.")
    else:
        st.write("The customer is likely to stay.")
