



import pandas as pd

df = pd.read_csv('df6.csv')

df['Score'] = df['Score'].clip(lower=65,
                               upper=100)

print(df)




