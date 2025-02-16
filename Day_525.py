

import pandas as pd

df = pd.read_csv('duplicates.csv')

print(df)
# print(df.duplicated())

unique_df = df.drop_duplicates()
print(unique_df)







