

import polars as pl

df = pl.read_csv('sorting.csv')

# print(df)

renamed_col = df.rename({'Name':'Student',
                         'Subject':'Class',
                         'Grade':'Score'})

print(renamed_col)
















