


import pandas as pd

df = pd.read_csv('temps.csv')

# print(df)

df['Temp'].fillna(df['Temp'].mean(), inplace=True)
# df['Temp'] = df['Temp'].fillna(df['Temp'].mean())

print(df)