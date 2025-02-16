




import pandas as pd

df = pd.read_csv('data.csv')

for index, row in df.iterrows():
    print(row['Date'])






























