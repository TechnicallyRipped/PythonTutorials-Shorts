



import streamlit as st

def clicked():
    st.write('Clicked!')

x = st.button('Click Me',
              on_click=clicked)

print(x)




















