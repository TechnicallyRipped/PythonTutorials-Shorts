

import pandas as pd

df = pd.read_csv('df_5.csv')

print(df)

print(df.nunique(axis=0)) #Unique values in each column
print(df.nunique(axis=1)) #Unique values in each row

