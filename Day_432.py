

import pandas as pd

df = pd.read_csv('cars.csv')
# print(df)

mileage = df['Mileage']

# print(mileage.describe())
print(mileage.min())
print(mileage.max())
