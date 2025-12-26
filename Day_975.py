

import pandas as pd

df = pd.read_csv('df__1.csv')
# print(df)

x = "State == 'NY' and Score == 100"

df2 = df.query(x)
print(df2)



