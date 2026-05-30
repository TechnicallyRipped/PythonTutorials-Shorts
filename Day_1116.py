

import pandas as pd

df = pd.read_csv('g1.csv')
df2 = pd.read_csv('df__1.csv')

print(df.head(1))
print(df2.head(1))

x = df2.columns.difference(df.columns).tolist()

print(x)