

import polars as pl

df = pl.read_csv('data.csv')

# print(df)

df = df.with_columns(Date2 = df['Date'].str.to_date())

# print(df)

df = df.with_columns(Date3 = df['Date2'].dt.('%m/%Y'))

print(df)

















