


import pandas as pd

df = pd.read_csv('csum.csv')

df['Total_Saved'] = df['Savings'].expanding().sum()

print(df)

# .mean()
# .sum()
# .min()
# .max()
# .count()
# .median()
















