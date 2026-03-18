


import polars as pl

df = pl.read_csv('p.csv')

df = df.with_columns(
    points2 = pl.col('points').cast(pl.String),
    points3 = pl.col('points').cast(pl.Float64)
)

print(df)
