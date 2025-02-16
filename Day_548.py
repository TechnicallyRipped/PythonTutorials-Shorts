# pip install streamlit

import streamlit as st

code = '''
def my_function():
    print('You ran my function!')'''

st.write("Look at this python code!")

st.code(code,language='python')

code2 = '''
SELECT *
FROM my_table'''

st.code(code2,language='SQL')

code3 = '''
x <- 'Hello World'
print(x)'''

st.code(code3,language='r')