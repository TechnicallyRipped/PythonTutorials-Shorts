

import pandas as pd

df = pd.read_csv('n1.csv')
# print(df)

df[['F','L']] = df['Name'].str.split(' ',
                                     expand=True)
print(df)
