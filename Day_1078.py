



import pandas as pd

df = pd.read_csv('df__2.csv')

names = df['Name'].tolist()

print(names)
print(type(names))
