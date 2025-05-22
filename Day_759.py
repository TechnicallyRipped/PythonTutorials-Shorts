


import pandas as pd

df = pd.read_csv('df_1.csv')

df['Score'] = df['Score'].mask(df['Score'] < 65,0)

print(df)