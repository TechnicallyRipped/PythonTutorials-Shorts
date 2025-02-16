

import pandas as pd

df = pd.read_csv('pass_fail.csv')

print(df)

crosstab_df = pd.crosstab(df['Name'], df['Pass_Fail'],
                          normalize='index')

print(crosstab_df)