


import polars as pl

df = pl.read_csv('duplicates.csv')

for row in df.rows():
    print(row[0])













