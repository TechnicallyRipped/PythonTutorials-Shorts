

import polars as pl

df = pl.read_csv('sorting.csv')

# print(df)

sorted_df = df.sort(['Name','Subject'])


print(sorted_df)












