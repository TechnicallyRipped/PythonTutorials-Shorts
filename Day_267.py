

import pandas as pd

df = pd.read_csv('long_df.csv')

print(df)

df_wide = df.pivot_table(index=['Name'], 
                         columns='Subject', 
                         values='Score').reset_index()
print('\n')
print(df_wide)


















