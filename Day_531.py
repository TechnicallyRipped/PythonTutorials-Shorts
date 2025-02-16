

import pandas as pd

df = pd.read_csv('piv_tbl.csv')

print(df)

pivot_df = pd.pivot_table(df, values='Sales', 
                          index='Region',
                          columns='Product', 
                          aggfunc=['sum','mean'])
print(pivot_df)







