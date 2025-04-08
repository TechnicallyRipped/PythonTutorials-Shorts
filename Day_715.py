

import polars as pl

df = pl.read_csv('whenthen.csv')

df = df.with_columns([pl.when(pl.col('Grade') >= 65)
                        .then(pl.lit('Pass'))
                        .otherwise(pl.lit('Fail'))
                        .alias('Pass_Fail')])

print(df)


