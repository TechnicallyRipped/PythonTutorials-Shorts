


import polars as pl

df = pl.read_csv('df7.csv')

df = df.with_row_index('myIndex')

print(df)







