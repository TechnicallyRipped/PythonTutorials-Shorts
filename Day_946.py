

import polars as pl

a = pl.DataFrame({'ID':[1,2,3,4],
                  'VALUE':['a','b','c','d']})

b = pl.DataFrame({'ID':[2,4],
                  'SUB_ID':['2.7','4.5']})

anti = a.join(b, on='ID', how='anti')

print(anti)






