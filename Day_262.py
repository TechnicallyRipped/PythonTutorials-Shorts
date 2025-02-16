


import pandas as pd

df = pd.read_csv('query.csv')
# print(df)

query = df.query("State == 'New York' ")
print(query)


















