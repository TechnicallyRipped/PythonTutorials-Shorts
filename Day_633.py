


import pandas as pd

df = pd.read_csv('df_1.csv')
print(df)

df2 = df.set_index('Name') 
print(df2)

df3 = df2.reset_index()
print(df3)



