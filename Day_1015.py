

import pandas as pd

df = pd.read_csv('grades_.csv')

subs = ['Math','Science']

df['Sub_Cat'] = pd.Categorical(df['Subject'],
                            categories=subs)

print(df)
