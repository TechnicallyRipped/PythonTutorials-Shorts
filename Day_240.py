

import pandas as pd

df = pd.read_csv('name-age.csv')

print(df)

df.rename(columns={'Age':'A','Height':'H'}
          ,inplace=True)

print(df)





















