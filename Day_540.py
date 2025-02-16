

import pandas as pd

df = pd.read_csv('rounds.csv')

df['Score'] = pd.to_numeric(df['Score'],
                            errors='coerce')

df['Score'] = df['Score'].round(2)
print(df)