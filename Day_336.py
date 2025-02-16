



import polars as pl

df = pl.read_csv('data.csv')

filtered = df.filter((df['Price'] > 15) &
                     (df['Price'] < 17))

print(filtered)















