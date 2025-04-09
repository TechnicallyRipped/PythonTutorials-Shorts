
import polars as pl

df = pl.read_csv('whenthen.csv')

df = df.with_columns([pl.when(pl.col('Grade') >= 95)
                        .then(pl.lit('A'))
                        .when(pl.col('Grade') >= 85)
                        .then(pl.lit('B'))
                        .when(pl.col('Grade') >= 75)
                        .then(pl.lit('C'))
                        .when(pl.col('Grade') >= 65)
                        .then(pl.lit('D'))
                        .otherwise(pl.lit('F'))
                        .alias('Letter_Grade')])
print(df)


