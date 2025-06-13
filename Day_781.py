

import streamlit as st

happy_mode = st.toggle("Happy Mode")

if happy_mode:
    st.write("Happy Mode is ON")
    st.image("happy.png")
else:
    st.write("Happy mode is OFF")
    st.image("sad.png")

