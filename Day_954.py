

import polars as pl

x = pl.DataFrame({
    'A':[1,2,3],
    'B':[4,5,6]})

y = pl.DataFrame({
    'A':[1,3,2],
    'B':[4,6,5]})

x = x.sort(by=x.columns)
y = y.sort(by=y.columns)

print(x.equals(y))





