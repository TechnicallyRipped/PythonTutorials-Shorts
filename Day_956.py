


import polars as pl

df = pl.read_csv('4colDF.csv')

df = df.select(
    pl.exclude('C'),
    pl.col('C')
)

print(df)





