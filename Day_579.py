


import pandas as pd

df = pd.read_csv('df_1.csv')

# print(df)

new_order = ['State','Name','Test_Score']

df2 = df[new_order]

print(df2)