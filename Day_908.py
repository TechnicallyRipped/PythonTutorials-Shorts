

import pandas as pd

df = pd.read_csv('null_.csv')

to_fill = ['Score1','Score2']
df[to_fill] = df[to_fill].fillna(100)

print(df)


