



import pandas as pd

df = pd.read_csv('cars.csv')

df.to_excel('cars.xlsx', index=False)

