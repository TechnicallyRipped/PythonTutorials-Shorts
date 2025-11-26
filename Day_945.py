

import polars as pl

x = pl.DataFrame({'ID':[1,2,3,4],
                  'VALUE':['a','b','c','d']})

y = pl.DataFrame({'ID':[2,4],
                  'SUB_ID':['2.7','4.5']})

semi = x.join(y, on='ID', how='semi')

print(semi)






