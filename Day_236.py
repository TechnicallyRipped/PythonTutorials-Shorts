



import pandas as pd

df = pd.read_csv('name-age.csv')

def add_5(x):
    return x+5

df['Age'] = df['Age'].apply(add_5)

print(df)





















