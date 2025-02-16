
# pip install streamlit


import matplotlib.pyplot as plt
import streamlit as st

x = [1,2,3,4,5,6]
y = [0,1,2,4,8,10]

plt.plot(x,y)
plt.title('Matplotlib Graph')
# plt.show()

st.pyplot(plt)
