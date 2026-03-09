
import polars as pl

df = pl.read_csv('risks.csv')

order = ['Low','Medium','High']

df = df.with_columns(
    pl.col("Risk")
    .cast(pl.Enum(order))
)

df = df.sort(by=['Risk'])

print(df)