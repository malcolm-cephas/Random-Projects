# 08_E2E_Delay_System/app/streamlit_app.py
import streamlit as st
import joblib
import pandas as pd
import os
import numpy as np

# Set up page
st.set_page_config(page_title="Flight Delay Predictor", page_icon="✈️")

st.title("✈️ Airline Delay Prediction Tool")
st.markdown("""
This app uses a **Machine Learning model** (Random Forest) to predict the probability of a flight delay 
based on historical trends, time of day, and carrier performance.
""")

# Load model
base_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(base_dir, '../../01_Flight_Delay_Prediction/models/delay_predictor_rf.joblib')
features_path = os.path.join(base_dir, '../../01_Flight_Delay_Prediction/models/feature_names.joblib')

@st.cache_resource
def load_assets():
    model = joblib.load(model_path)
    features = joblib.load(features_path)
    return model, features

try:
    model, feature_names = load_assets()
    
    # Sidebar for inputs
    st.sidebar.header("Flight Details")
    hour = st.sidebar.slider("Scheduled Departure Hour (24h)", 0, 23, 12)
    day = st.sidebar.selectbox("Day of Week", options=[0,1,2,3,4,5,6], format_func=lambda x: ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"][x])
    distance = st.sidebar.number_input("Flight Distance (miles)", 100, 5000, 1000)
    carrier = st.sidebar.selectbox("Carrier", ["AA", "DL", "UA", "WN", "AS", "B6"])
    
    # Prediction Button
    if st.button("Predict Delay Probability"):
        # Prepare input data (Match one-hot encoding of training)
        input_data = pd.DataFrame(columns=feature_names)
        input_data.loc[0] = 0
        
        input_data.at[0, 'hour'] = hour
        input_data.at[0, 'day_of_week'] = day
        input_data.at[0, 'distance'] = distance
        
        # Set carrier flag
        carrier_col = f'carrier_{carrier}'
        if carrier_col in input_data.columns:
            input_data.at[0, carrier_col] = 1
            
        # Predict
        prob = model.predict_proba(input_data)[0][1]
        
        # Display Result
        st.subheader("Result:")
        if prob > 0.5:
            st.error(f"High Risk of Delay! Probability: {prob:.1%}")
        else:
            st.success(f"Likely On-Time. Probability of Delay: {prob:.1%}")
            
except Exception as e:
    st.warning("Model files not found. Please run Project 1 model training first.")
    st.error(e)
