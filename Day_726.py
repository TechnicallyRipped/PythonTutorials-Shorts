


import polars as pl

df = pl.read_csv('cols2.csv')

x = df.get_column_index('Score')

print(x)



