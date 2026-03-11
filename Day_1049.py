

import polars as pl

df = pl.read_csv('df__2.csv')

print(df)

maxScore = df['Score'].max()
print(maxScore)

minScore = df['Score'].min()
print(minScore)






