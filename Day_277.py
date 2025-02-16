






import pandas as pd

df = pd.read_csv('split.csv')

df[['First','Last']] = df['Name'].str.split(n=1,expand=True)

df.drop(columns=['Name'], inplace=True)

print(df)























