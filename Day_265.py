


import pandas as pd

df = pd.read_csv('grades.csv')

df['Date'] = pd.to_datetime(df['Date'])

print(df)
print(df.dtypes)


















