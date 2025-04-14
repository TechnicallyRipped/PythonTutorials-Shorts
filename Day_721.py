



import polars as pl

df = pl.read_csv('fill_vals.csv')

df = df.with_columns(pl.col('Score')
                     .fill_null(strategy="backward")
                     .alias('Filled'))
print(df)







