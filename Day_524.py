

import pandas as pd

df = pd.read_csv('roll.csv')

df['3D_Avg'] = df['Sales'].rolling(window=3).mean()

df['3D_Sum'] = df['Sales'].rolling(window=3).sum()

print(df)







