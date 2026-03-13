

import polars as pl

df = pl.DataFrame({
    "a": [None, None, 7],
    "b": [3, None, None],
    "c": [8, 6, 2]
})

df = df.with_columns(
    COAL = pl.coalesce(['a','b','c'])
)

print(df)