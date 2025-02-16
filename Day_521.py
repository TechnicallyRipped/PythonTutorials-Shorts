

import pandas as pd

df = pd.read_csv('df.csv')

df['Rank'] = df['Grade'].rank()

print(df)
