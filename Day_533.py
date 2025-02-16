

import pandas as pd

df = pd.read_csv('john.csv')
df2 = pd.read_csv('chris.csv')

# print(df)
# print(df2)

join_df = pd.concat([df,df2],axis=1)
print(join_df)


