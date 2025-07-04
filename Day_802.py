

import pandas as pd

df = pd.read_csv('fruits.csv')

# print(df)

df2 = df[['Fruit','Price']].drop_duplicates()
print(df2)