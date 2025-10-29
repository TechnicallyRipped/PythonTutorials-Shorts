


import pandas as pd

df1 = pd.read_csv('k1.csv')
df2 = pd.read_csv('k2.csv')

merged_df = pd.merge(df1,df2,
                     on=['id'],
                     suffixes=['_test1',
                               '_test2'])

print(merged_df)



