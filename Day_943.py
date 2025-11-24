

import polars as pl

df = pl.read_csv('points1.csv')

df = df.with_columns(
    pl.col("Point").str.json_extract()
)

df = df.unnest('Point')

print(df)







