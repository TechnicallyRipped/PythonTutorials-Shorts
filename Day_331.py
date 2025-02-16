


import polars as pl

df = pl.read_csv('grades.csv')

# print(df)


df.drop_in_place('Name')

print(df)








