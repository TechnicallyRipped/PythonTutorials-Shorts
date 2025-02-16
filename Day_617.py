


import pandas as pd

df = pd.read_csv('some_null.csv')
# print(df)

df2 = df.fillna(value={'Age':999,
                       'Score':100})
print(df2)












