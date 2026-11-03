

import pandas as pd

df = pd.read_csv('df__2.csv')

df['Passing'] = df['Score'] >= 65

print(df)
