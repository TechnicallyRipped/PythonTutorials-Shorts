



import pandas as pd

df = pd.read_csv('null.csv')

df2 = df.fillna('111', inplace=False)

print(df2)























