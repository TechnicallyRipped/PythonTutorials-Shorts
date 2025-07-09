


import pandas as pd

df = pd.read_csv('df_items.csv')

# print(df)

print(df['Price'].idxmin())
print(df['Price'].idxmax())