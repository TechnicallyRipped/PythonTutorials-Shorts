

import polars as pl

df = pl.read_csv('sorting.csv')

# print(df)

df = df.with_columns(Shifted=df['Grade'].shift(-2)
                     .fill_null('SHIFTED'))

print(df)


















