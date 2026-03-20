

import pandas as pd

df = pd.read_csv('p2.csv')

# print(df)
x = df.select_dtypes(include=['int',
                              'float'])

print(x)