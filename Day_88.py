


import pandas as pd

df = pd.read_csv('duplicates.csv')

f_df = df[df['Name'] != 'Mario']

print(f_df)











































