

import polars as pl

df = pl.read_csv('roll.csv')

df = df.with_columns(Avg_3D = pl.col('Sales').rolling_mean(window_size=3),
                     Sum_3D = pl.col('Sales').rolling_sum(window_size=3),
                     Max_3D = pl.col('Sales').rolling_max(window_size=3),)

print(df)