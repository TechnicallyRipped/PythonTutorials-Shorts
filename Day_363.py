

import polars as pl

df = pl.read_csv('pipe_sep.txt'
                 ,separator='|')

print(df)


















