
import streamlit as st
import pandas as pd
import os

st.title("User Info Form")
csv_path = 'st_test.csv'

with st.form("user_form"):
    name = st.text_input("Name")
    age = st.number_input("Age")
    submit_button = st.form_submit_button("Submit")
    form_data = {'Name':name, 'Age':age}

if submit_button:
    df = pd.DataFrame([form_data])
    if os.path.exists(csv_path):
        existing_df = pd.read_csv(csv_path)
        updated_df = pd.concat([existing_df, df],
                               ignore_index=True)
        updated_df.to_csv(csv_path,index=False)
        st.success("New row added to file!")
    else:
        df.to_csv(csv_path, index=False)
        st.success("New file created!")

