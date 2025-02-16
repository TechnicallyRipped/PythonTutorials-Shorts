

import pandas as pd

df = pd.read_csv('date_df.csv')

df['Date'] = pd.to_datetime(df['Date'])

df['year'] = df['Date'].dt.strftime('%Y')

df['Date2'] = df['Date'].dt.strftime('%m-%d-%Y')

print(df)















