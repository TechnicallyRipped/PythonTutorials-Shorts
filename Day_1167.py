


import pandas as pd

df = pd.read_csv('dfStr.csv')

df['id'] = df['id'].str.upper()
df['name'] = df['name'].str.capitalize()
df['state'] = df['state'].str.title()
df['division'] = df['division'].str.lower()
print(df)
