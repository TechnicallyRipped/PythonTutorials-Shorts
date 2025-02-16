


import pandas as pd

df = pd.read_csv('foods.csv')

df['Day'] = pd.to_datetime(df['Day'])

df['EatBy'] = df['Day'] + pd.Timedelta(weeks=-5)

print(df)
