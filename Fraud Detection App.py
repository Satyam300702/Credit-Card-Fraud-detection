# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 07:54:29 2025

@author: HP
"""

import os
import numpy as np
import streamlit as st
import pickle

model_path = os.path.join(os.path.dirname(__file__),"fraud.sav")
try:
    fraud = pickle.load(open(model_path,"rb"))
except FileNotFoundError:
    st.error("Model file not found")
    st.stop()
    
def Fraud_detection(input_data): 
    input_data_as_numpy_array = np.asarray(input_data).reshape(1,-1)
    prediction = fraud.predict(input_data_as_numpy_array)
    probability = fraud.predict_proba(input_data_as_numpy_array)[0][1]
    
    if prediction[0] ==1:
        return f"⚠️ Transaction is Fraudulent\nProbability: `{probability:.4f}`"
    else:
        return f"✅ Transaction is Safe\nProbability: `{probability:.4f}`"
    
def main():
    st.title("Credit Card Fraud Detection App")
    st.write("""
             ### 💳 About the App
             This app uses a Machine Learning model to detect whether a credit card transaction is **fraudulent or genuine** based on 28 anonymized transaction features and the transaction amount.
             """)
    
    V = []
    for i in range(1,29):
        V_i = st.number_input(f"V{i}")
        V.append(V_i)
        
    Amount = st.number_input("Amount")
    
    result = ""
    if st.button("Predict"):
        input_list = V + [Amount]
        result = Fraud_detection(input_list)
        
    st.success(result)
if __name__ == "__main__":
    main()
