import streamlit as st
from fastapi import FastAPI
import requests
import json

st.write("Calculator")
option = st.selectbox(
    'How would you like to be contacted?',
    ('addition', 'subtraction', 'multiplication','divsion'))


st.write('You selected:', option)
st.write("Enter 2 numbers")
number1 = st.number_input('Enter the 1st number')
number2=st.number_input('Enter the 2nd number')
print(number1,number2)
op={'operation':option,'x':number1,'y':number2}
print(json.dumps(op))
if st.button("Calculate"):
    result=requests.post(url = "http://localhost:8000/calculate", 
              data = json.dumps(op))
    st.write((result.text))