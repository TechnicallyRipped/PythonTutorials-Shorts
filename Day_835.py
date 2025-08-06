
import streamlit as st

st.title("Website Stats")

st.metric(label="Monthly Visits", value="10,000",
          delta="+8%")

st.metric(label="Weekly Visits", value="2,000",
          delta="-20%")

st.metric(label="Customer Acquisition Cost",
          value="$12.00", delta="-25%",
          delta_color='inverse')


