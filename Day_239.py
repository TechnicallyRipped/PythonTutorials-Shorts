


import pandas as pd

df = pd.read_csv('name-age.csv')

df.sort_values(by='Age',inplace=True,
               ascending=False)

print(df)





















