

import pandas as pd

df = pd.read_csv('df__1.csv')
# print(df)

df[['A','B']] = 1,2
print(df)
