

import pandas as pd

df = pd.read_csv('df__1.csv')
print(df)

names = df['Name'].unique()
print(names)

n = df['Name'].nunique()
print(n)