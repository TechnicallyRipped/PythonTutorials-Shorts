

import pandas as pd 

df = pd.read_csv('df_1.csv')

df['Curve_Score'] = df['Test_Score'] + 5

# print(df)
df.to_csv('curved.csv',
          columns=['Name','State','Curve_Score'],
          index=False)


