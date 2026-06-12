

import pandas as pd
df = pd.read_csv('add.csv')

df['C'] = df['A'] + df['B']

print(df)

import polars as pl
df2 = pl.read_csv('add.csv')

df2 = df2.with_columns(
    C = pl.col('A') + pl.col('B')
    )

print(df2)