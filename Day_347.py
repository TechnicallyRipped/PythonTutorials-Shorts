

# pip install xlsx2csv

import polars as pl

df = pl.read_excel('data2.xlsx',sheet_name='Sheet2')

print(df)














