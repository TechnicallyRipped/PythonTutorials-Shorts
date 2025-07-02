

import pandas as pd

df = pd.read_csv('monthly_sales.csv')

df['Change'] = df['Sales'].pct_change()
df['Change2'] = df['Sales'].pct_change(2)

print(df)