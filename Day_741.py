

import pandas as pd

df1 = pd.read_csv('comb1.csv')
df2 = pd.read_csv('comb2.csv')

df3 = df1.combine_first(df2)
print(df3)
