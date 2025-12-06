


import polars as pl

df = pl.read_csv('4colDF.csv')

df = df.select(sorted(df.columns,
                      reverse=True))

print(df)





