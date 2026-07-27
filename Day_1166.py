

import pandas as pd

df = pd.read_csv('dfL.csv')
# print(df)

front = ['Name','TotalScore']

back = [i for i in df.columns if i not in front]

df = df[front + back]

print(df)