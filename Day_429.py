

import pandas as pd

df = pd.read_csv('duplicates.csv')

# df.drop_duplicates(inplace=True)
df2 = df.drop_duplicates()

print(df2)

