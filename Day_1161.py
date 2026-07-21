

import pandas as pd

df = pd.read_csv('ex5.csv')

print(df)

print(df[df.duplicated()])
print(df.isna().sum())

df2 = df.sort_values(["Department", "Salary"],
                     ascending=[True, False])
print(df2)