

import streamlit as st

age = st.slider("Select your age", 
                min_value=0,
                max_value=100,
                value=50,
                step=10)


st.write(f"Age: {age}")
