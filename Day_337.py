



import polars as pl

df1 = pl.DataFrame({
    'key': ['A', 'B', 'C', 'D'],
    'value_left': [1, 2, 3, 4]
})

df2 = pl.DataFrame({
    'key': ['B', 'C', 'D', 'E'],
    'value_right': [5, 6, 7, 8]
})

joined_df = df1.join(df2, on=['key'],how='left')

print(joined_df)















