



import pandas as pd

df = pd.read_csv('duplicates.csv')

name_list = df['Name'].unique()

print(name_list)



















































