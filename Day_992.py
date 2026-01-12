
import pandas as pd

df = pd.read_csv('sal.csv')

# print(df)

result = df.sort_values(by=['salary'],ascending=False)

result = result.drop_duplicates(subset=['first_name'])

print(result)