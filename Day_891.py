

import pandas as pd

df = pd.read_csv('filterScore.csv')

# print(df)

gt90 = df[df['Score'] >= 90]
print(gt90)