

import polars as pl

df = pl.read_csv('quote.csv')

df = df.with_columns(
    L = pl.col('Quote').str.len_chars()
)

print(df)