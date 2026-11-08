

import pandas as pd

df = pd.read_csv('inv.csv')
print(df)

v = df['Type'].value_counts()
print(v)