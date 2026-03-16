

import polars as pl

df = pl.read_csv('p.csv')

df = df.with_columns(
    name = 'Player: ' + pl.col('name'),
    points = pl.col('points').cast(pl.String)
             + ' points'
)

print(df)