

import pandas as pd

df1 = pd.read_csv('df_1.csv')

df2 = pd.read_csv('df_1.csv')

df2['Score'] = df2['Score'].astype('str')

print(df1.equals(df2))
