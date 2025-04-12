

import polars as pl

df = pl.read_csv('df6.csv')

df = df.with_columns([
    pl.col('Name').str.to_uppercase().alias('upper'),
    pl.col('Name').str.to_lowercase().alias('lower'),
    pl.col('Name').str.to_titlecase().alias('cap'),
    ])

print(df)





