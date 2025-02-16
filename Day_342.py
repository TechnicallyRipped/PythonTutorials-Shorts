

import polars as pl

df = pl.read_csv('nulls.csv')

# print(df)

fill_df = df.fill_null('NULL_STRING').fill_null(0)

# print(fill_df)

drop_df = df.drop_nulls()

print(drop_df)

















