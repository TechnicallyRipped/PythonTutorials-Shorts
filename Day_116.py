

import pandas as pd


df1 = pd.read_csv('left_data.csv')
df2 = pd.read_csv('right_data.csv')

merged_df = pd.merge(df1, df2, on=['name', 'lname'])

print(merged_df)



