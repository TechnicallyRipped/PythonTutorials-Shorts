



import pandas as pd

df = pd.read_csv('name-age.csv')

print(df)

sub_df = df.iloc[2:,:2]

print(sub_df)


























