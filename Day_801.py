

import pandas as pd
import streamlit as st

df = pd.read_csv('df.csv')

st.dataframe(df,
             hide_index=True,
             column_order=['Grade','Subject'])
