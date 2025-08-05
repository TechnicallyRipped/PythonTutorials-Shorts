
import plotly.express as px
import streamlit as st

x_vals = ['A','B','C']
y_vals = [100,125,150]

fig = px.bar(x=x_vals, y=y_vals)

st.title("Streamlit + Plotly")

st.plotly_chart(fig,use_container_width=True)
