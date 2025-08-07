
import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'Name': ['Mike', 'Brian', 'Chris'],
    'Age': [25, 30, 35]
})

csv = df.to_csv(index=False).encode('utf-8')

st.download_button(label="Download CSV",
                   data=csv,
                   file_name='my_df.csv')
