


import polars as pl

df = pl.read_csv('df7.csv')

string_df = df.select(pl.col(pl.String))
print(string_df)

num_df = df.select(pl.col(pl.Int64))
print(num_df)


