

import polars as pl 

df = pl.read_csv('df_1.csv')

pandas_df = df.to_pandas()
# print(type(pandas_df))

polars_df = pl.from_pandas(pandas_df)
print(type(polars_df))








