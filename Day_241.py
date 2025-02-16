

import pandas as pd

df = pd.read_csv('name-age.csv')

print(df)

df = df.rename(columns={'Name':'AA'})

print(df)




















