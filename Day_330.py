


import polars as pl

df = pl.read_csv('duplicates.csv')

# print(df)

score_values = pl.Series([95,99,94,90,96])

df = df.with_columns(Score = pl.lit(score_values),
                     Score_x2 = pl.lit(score_values*2))


print(df)












