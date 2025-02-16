


import pandas as pd

df1 = pd.read_csv('L_join1.csv')
df2 = pd.read_csv('L_join2.csv')

print(df1)
print(df2)

left_df = pd.merge(df1,df2,how='left',
                   left_on=['Name'],
                   right_on=['Name'])

print(left_df)





