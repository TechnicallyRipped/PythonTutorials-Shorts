

import pandas as pd

df = pd.read_csv('df__1.csv')
print(df)

df = df.iloc[::-1]
print(df)