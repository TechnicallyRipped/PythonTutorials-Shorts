

import polars as pl

df = pl.read_csv('test_scores.csv')

df_long = df.melt(id_vars=['Year','Name'],
                  variable_name='Subject',
                  value_name='Score')
print(df_long)

