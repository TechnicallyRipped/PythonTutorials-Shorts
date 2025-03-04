

import pandas as pd

df = pd.read_csv('bad_df.csv')

df.columns = df.columns.str.replace(" ","_")

print(df)









