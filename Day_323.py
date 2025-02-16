

import pandas as pd

df = pd.read_csv('bl_index.csv')
# print(df)

sub_df = df[(df['Score'] < 65) & (df['Subject'] == 'Math')]

print(sub_df)















