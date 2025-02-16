


import pandas as pd

df = pd.read_csv('duplicates.csv')

condition_1 = df['Name'] != 'Mario'
condition_2 = df['Age'] == 28

f_df = df[condition_1 & condition_2]

print(f_df)









































