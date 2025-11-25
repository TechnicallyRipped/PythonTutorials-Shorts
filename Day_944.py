
import polars as pl

df = pl.read_csv('prems.csv')

vals = {'H':'Home',
        'A':'Auto'}

df = df.with_columns(
    pl.col('Cov_Code').replace(vals,
                               default='N/A')
)

print(df)

