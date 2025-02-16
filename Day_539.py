

import pandas as pd

df = pd.read_csv('whsp.csv')

df['Name'] = df['Name'].str.rstrip()

print(df)
print(len(df['Name'][1]))
