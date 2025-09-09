
import pandas as pd

df = pd.read_csv('df__1.csv')

df['Score2'] = df['Score'].copy()
df['Score2'][0] = 100

print(df)