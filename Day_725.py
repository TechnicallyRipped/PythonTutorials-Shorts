


import pandas as pd

df = pd.read_csv('c.csv')


df['Value'] = df['col1'].combine_first(df['col2'])

print(df)







