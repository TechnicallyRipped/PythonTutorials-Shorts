
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('fruit_sales.csv')
fruits = df['Fruit'].unique()

fruit_filter = st.selectbox("Select a fruit", fruits)
filtered_df = df[df['Fruit'] == fruit_filter]

fig,ax = plt.subplots()
ax.plot(filtered_df['Month'],
        filtered_df['Sales'])

ax.set_xlabel('Month')
ax.set_ylabel('Sales')

st.pyplot(fig)