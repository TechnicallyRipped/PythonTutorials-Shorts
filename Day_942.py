

import polars as pl

df = pl.read_csv('points.csv')

df = df.with_columns(
    pl.struct(['X','Y']).alias('Point')
    )

# print(df)
print(df.select(pl.col("Point").struct.field("X")))














# df = df.with_columns(
#     pl.col('Point').struct.rename_fields(["new_x", "new_y"])
# )

# df = df.unnest('Point')

# print(df)