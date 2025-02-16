

import polars as pl

df = pl.read_csv('sorting.csv')

# print(df)

df.write_csv('df.csv')














