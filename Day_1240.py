

import pandas as pd

df = pd.read_csv('df__1.csv')
print(df)

i = df.index[df['Name'] == 'John']
print(i)
