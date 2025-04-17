


import polars as pl

df = pl.read_csv('hobby.csv')

df = df.with_columns(
    pl.col('Hobbies').str.split(",")
).explode('Hobbies')

print(df)







