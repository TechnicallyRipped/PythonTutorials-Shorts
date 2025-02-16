

import streamlit as st

x = st.radio("Choose your favorite color:",
             options=["Red", "Blue", "Green", "Yellow"],
             index=1,
             help="Subscribe?")

st.write(f"Selected: {x}")

print(x)