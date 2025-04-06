

import pandas as pd

df1 = pd.read_csv('l_join1.csv')
df2 = pd.read_csv('l_join2.csv')

df3 = pd.merge(df1, df2, on=['Name'], how='outer')

print(df3)

