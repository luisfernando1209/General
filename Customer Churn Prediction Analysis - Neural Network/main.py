import streamlit as st
import requests

st.title("Churn Prediction Analysis")

tenure = st.number_input("Input tenure",min_value = 0)
MonthlyCharges = st.number_input("Input Monthly Charges",min_value = 0.0)
TotalCharges = st.number_input("Input Total Charges",min_value = MonthlyCharges)
OnlineSecurity = st.radio("Online security",["Yes","No","No internet service"])
Contract = st.radio("Contract",["Two year","One year","Month-to-month"])
PaymentMethod = st.radio("Payment method",['Electronic check' ,'Mailed check' ,'Bank transfer (automatic)', 'Credit card (automatic)'])




URL =  "https://p2m1-backend-new.herokuapp.com/churn"
data ={
    'tenure':tenure,
    'MonthlyCharges':MonthlyCharges,
    'TotalCharges':TotalCharges,
    'OnlineSecurity':OnlineSecurity,
    'Contract':Contract,
    'PaymentMethod':PaymentMethod
        }
r = requests.post(URL, json=data)
res = r.json()
show_result = st.radio("Show result?",["Yes","No"],index=1)
if show_result == "Yes":
    st.title(res['result']['classes'])
