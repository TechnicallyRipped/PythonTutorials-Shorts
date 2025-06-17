

import pandas as pd

df1 = pd.read_csv('df_items.csv')

df2 = df1.copy()

df1['Total'] = df1['Price'] * df1['Quantity']

print(df1)
print(df2)


