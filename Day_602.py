


import pandas as pd

df = pd.read_csv('fill_vals.csv')

df['forward'] = df['Value'].ffill(limit=1)
df['backward'] = df['Value'].bfill(limit=1)

print(df)






