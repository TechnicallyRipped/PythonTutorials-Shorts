


import pandas as pd

df = pd.read_csv('profit.csv')
print(df)

sales_df = df.filter(like='sales')
print(sales_df)

q1_df = df.filter(like='q1')
print(q1_df)





