

import polars as pl

df = pl.DataFrame({
    "first": ["Kyle", "Joe", "Craig"],
    "last": [67,400,20]
})

df = df.with_columns(
    full_name = pl.concat_str(["first", "last"], separator=" ")
)

print(df)