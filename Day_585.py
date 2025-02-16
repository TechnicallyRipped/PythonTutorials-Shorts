

# pip install polars

import polars as pl

df = pl.read_csv('df.csv')

df2 = df.with_columns(
    pl.col("Grade").rank("dense",
                         descending=True).alias("Highest"))

print(df2)






















