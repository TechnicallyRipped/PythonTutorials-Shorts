

import polars as pl

df = pl.read_csv('calories.csv')

df2 = df.group_by(['Name']).agg(
    sum_ = pl.col('Calories').sum(),
    count_ = pl.col('Calories').count()
)

print(df2)















