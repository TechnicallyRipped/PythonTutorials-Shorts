


import pandas as pd


df = pd.read_csv('output.csv')

for index, row in df.iterrows():
    print(row[1])















































