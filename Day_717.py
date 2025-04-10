


import polars as pl

df = pl.read_csv('df6.csv')

df = df.filter(pl.col('Name').is_in(['Chris','Joe']))

print(df)


