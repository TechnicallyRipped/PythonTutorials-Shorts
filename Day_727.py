

import polars as pl

df = pl.read_csv('df7.csv')
df2 = pl.read_csv('df8.csv')

df3 = df.vstack(df2)
print(df3)

