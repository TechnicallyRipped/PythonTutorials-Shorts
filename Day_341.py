

import polars as pl

df = pl.read_csv('cars.csv')

# print(df)

my_df = df.select(['Model','Mileage'])

print(my_df)
















