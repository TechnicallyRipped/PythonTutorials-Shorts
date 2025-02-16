


import pandas as pd

df1 = pd.read_csv('df_1.csv')
df2 = pd.read_csv('df_2.csv')

# print(df1)
# print(df2)

df3 = pd.merge(df1,df2,on=['Name','State'])
print(df3)