

import pandas as pd

df = pd.read_csv('Book1.csv')

df['Date'] = pd.to_datetime(df['Date'])

# print(df)

df2 = df[df['Date'].between('2026-01-05','2026-01-08')]

print(df2)