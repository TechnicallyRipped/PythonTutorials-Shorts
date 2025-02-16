

import pandas as pd

df = pd.read_csv('duplicates.csv')

print(df)

print(df.nunique())
print(df['Name'].nunique())


