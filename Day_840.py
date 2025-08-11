
import streamlit as st
import time

st.title("Progress Bar Example")
start_button = st.button("Start Bar")

bar = st.progress(0)

if start_button:
    for i in range(101):
        time.sleep(0.05)
        bar.progress(i)
    st.success("Done!")
