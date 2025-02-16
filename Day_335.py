



import polars as pl

df = pl.read_csv('data.csv')

print(df)

x = df.to_pandas()

print(x)














