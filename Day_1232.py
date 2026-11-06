




import pandas as pd

df = pd.read_csv('df__1.csv')
print(df)

df = df.drop(columns=['Name'])
print(df)