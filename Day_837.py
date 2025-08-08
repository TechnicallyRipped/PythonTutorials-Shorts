
import streamlit as st
import pandas as pd

st.title("User Info Form")

with st.form("user_form"):
    name = st.text_input("Name")
    age = st.number_input("Age")
    submit_button = st.form_submit_button("Submit")
    form_data = {'Name':name, 'Age':age}

if submit_button:
    df = pd.DataFrame([form_data])
    df.to_csv('st_test.csv', index=False)
    st.success("Your response has been saved!")

