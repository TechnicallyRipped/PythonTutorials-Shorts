


import pandas as pd

df = pd.read_csv('ex1.csv',header=1)

# df.columns = df.iloc[0]
# df = df[1:]

print(df)
print(df.columns)
