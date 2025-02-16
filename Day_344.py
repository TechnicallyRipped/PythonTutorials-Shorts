

import polars as pl

df = pl.read_csv('data.csv')

# print(df)

df = df.with_columns(Price = df['Price'].cast(pl.Float64))

print(df)


















