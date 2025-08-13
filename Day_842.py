

import streamlit as st

st.title("Webcam")

img_file = st.camera_input("Capture an image")

if img_file:
    with open("streamlit_pic.png", "wb") as f:
        f.write(img_file.getvalue())
