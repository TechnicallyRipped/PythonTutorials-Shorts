

import streamlit as st
from datetime import date

x = st.date_input("Select a date",
                     value=date(2024, 11, 19),
                     min_value=date(2024, 11, 1),
                     max_value=date(2024, 12, 15))

st.write(f"You selected: {x}")



































