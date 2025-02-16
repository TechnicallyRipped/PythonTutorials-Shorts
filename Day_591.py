



import streamlit as st 

file = st.file_uploader("Choose a file",
                        type=["csv", "txt", "xlsx"],
                        accept_multiple_files=True)

# if file is not None:
#     st.write(f'You uploaded {file.name}')