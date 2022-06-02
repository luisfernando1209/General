import streamlit as st
import requests

st.title("Churn Prediction Analysis")

account_length = st.number_input("Input account length",min_value = 0)
iplan_radio = st.radio("Using international plan?",["Yes","No"])
total_day_minutes = st.number_input("Total day minutes",min_value = 0.0)
total_day_calls = st.number_input("Total day calls",min_value = 0)
total_eve_minutes = st.number_input("Total eve minutes",min_value=0.0)
total_night_minutes = st.number_input("Total night minutes",min_value=0.0)
total_night_calls = st.number_input("Total night calls",min_value = 0)
total_intl_minutes = st.number_input("Total international minutes",min_value = 0.0)
total_intl_calls = st.number_input("Total international calls",min_value=0)
customer_service_calls = st.number_input("Customer service calls",min_value=0)



URL = "https://luis-fernando-modelml2.herokuapp.com/churn"
data ={
    'Account length':account_length,
 'International plan':iplan_radio,
 'Total day minutes':total_day_minutes,
 'Total day calls':total_day_calls,
 'Total eve minutes':total_eve_minutes,
 'Total night minutes':total_night_minutes,
 'Total night calls':total_night_calls,
 'Total intl minutes':total_intl_minutes,
 'Total intl calls':total_intl_calls,
 'Customer service calls':customer_service_calls
        }
r = requests.post(URL, json=data)
res = r.json()
st.title(res['result']['classes'])