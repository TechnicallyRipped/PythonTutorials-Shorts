




import pandas as pd

df = pd.read_csv('duplicates.csv')

unique_df = df.drop_duplicates()

print(unique_df)































