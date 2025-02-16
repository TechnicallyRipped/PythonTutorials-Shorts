


# pip install streamlit

import streamlit as st

names = ['Chris','John','Joe']

choice = st.selectbox('Select a name:',
                      options=names,
                      index=1)

st.write(f'You selected: {choice}')
