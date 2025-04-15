


import polars as pl

df = pl.read_csv('df.csv')

df = df.drop(['Date','Subject']) # Method 1
df = df.select(pl.all().exclude(['Date','Subject'])) # Method 2

print(df)







