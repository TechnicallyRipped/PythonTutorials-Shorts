

import pandas as pd 

df = pd.read_csv('df_1.csv')
print(df)

mask = df['Test_Score'] > 90

x = df[~mask]

print(x)