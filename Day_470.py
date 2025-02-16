


import pandas as pd

df = pd.read_csv('some_null.csv')
# print(df)

na_df = df[df['Age'].isnull() | df['Score'].isnull()]
print(na_df)















