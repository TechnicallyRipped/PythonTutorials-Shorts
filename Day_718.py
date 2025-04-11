


import polars as pl

df = pl.read_csv('df.csv')

df = df.filter(pl.col('Grade').is_between(80,90))

print(df)






