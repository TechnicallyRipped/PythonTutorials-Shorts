

import polars as pl

df = pl.read_csv('dts.csv',
                 try_parse_dates=True)


df = df.with_columns(
    Days_Between = (
        pl.col("end") - pl.col("start")
        ).dt.total_days()
)

print(df)