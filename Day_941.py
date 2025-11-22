

import polars as pl

df = pl.read_csv('prems.csv')

cov_codes = {'H':'Home',
             'A':'Auto'}

df = df.with_columns(
    pl.col('Cov_Code').map_dict(cov_codes,
                                default='Uknown')
    .alias('Coverage')
)
print(df)