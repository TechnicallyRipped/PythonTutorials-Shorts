
import streamlit as st
import time

@st.cache_data
def load_data():
    time.sleep(3)
    return 'The data has loaded'

my_data = load_data()

st.write(f'Data: {my_data}')

st.radio('Pick one:',
         options=["A","B","C"])