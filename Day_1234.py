

import pandas as pd

df = pd.read_csv('miss.csv')

print(df)

m = df['Score'].isna().mean() * 100

print(m)