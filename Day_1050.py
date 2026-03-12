

import polars as pl

df = pl.DataFrame({
    "a": [5, 2, 7],
    "b": [3, 4, 1],
    "c": [8, 6, 2]
})

df = df.with_columns(
    Total = pl.col('a') + pl.col('b') + pl.col('c'),
    Total2 = pl.sum_horizontal('a','b','c')
)

print(df)