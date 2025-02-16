


import pandas as pd

df = pd.read_csv('date_df.csv')

df['Score2'] = df['Score'].shift(-1)

print(df)








