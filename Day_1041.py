

import pandas as pd

df = pd.read_csv('bigBack.csv')

long_df = pd.wide_to_long(
    df,
    stubnames="Sales",
    i="Store",
    j="Year",
    sep="_"
).reset_index()

print(long_df)
