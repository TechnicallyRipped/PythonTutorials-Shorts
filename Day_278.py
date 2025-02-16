


import pandas as pd

df = pd.read_csv('nulls.csv')

df.dropna(inplace=True,
          subset=['Age','Score'])

print(df)
























