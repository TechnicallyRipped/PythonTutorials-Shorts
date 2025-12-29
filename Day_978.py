

import pandas as pd

df = pd.read_csv('df6.csv')

s = pd.Series([35,25,29,30])

df['Age'] = s

print(df)

