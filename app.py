# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import streamlit as st
import pickle
import numpy as np

# 1. Load the trained model
filename = 'trained_model.sav'
model = pickle.load(open(filename, 'rb'))

# 2. Set up the App Header
st.title("Car Price Prediction App")
st.markdown("Enter the car details below to estimate the selling price.")

# 3. Create Input Fields for User
# Note: Ensure the order of features matches your 'X' columns exactly
# [Year, Present_Price, Kms_Driven, Fuel_Type, Seller_Type, Transmission, Owner]

col1, col2 = st.columns(2)

with col1:
    year = st.number_input("Year of Purchase", min_value=2000, max_value=2026, value=2015)
    present_price = st.number_input("Present Showroom Price (in Lakhs)", min_value=0.0, value=5.0)
    kms_driven = st.number_input("Kilometers Driven", min_value=0, value=20000)
    owner = st.selectbox("Number of Previous Owners", [0, 1, 3])

with col2:
    fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
    seller_type = st.selectbox("Seller Type", ["Dealer", "Individual"])
    transmission = st.selectbox("Transmission", ["Manual", "Automatic"])

# 4. Pre-process the User Input (Encoding)
# This must match the encoding used in your training script
fuel_dict = {'Petrol': 0, 'Diesel': 1, 'CNG': 2}
seller_dict = {'Dealer': 0, 'Individual': 1}
trans_dict = {'Manual': 0, 'Automatic': 1}

# Map strings to numbers
f_val = fuel_dict[fuel_type]
s_val = seller_dict[seller_type]
t_val = trans_dict[transmission]

# 5. Prediction Logic
if st.button("Predict Selling Price"):
    # Create an array for prediction
    features = np.array([[year, present_price, kms_driven, f_val, s_val, t_val, owner]])
    
    prediction = model.predict(features)
    
    # Output result
    st.success(f"The estimated selling price is: ₹ {prediction[0]:.2f} Lakhs")