

import polars as pl

df = pl.DataFrame({
    "week": [1,2,3,4,5,6,7,8],
    "sales": [10,12,15,13,10,14,17,18]
})
# print(df)

df = df.with_columns(
    FW_sales = pl.col("sales")
    .rolling_sum(window_size=4,
                 min_periods=1)
)
print(df)