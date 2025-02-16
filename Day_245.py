



import pandas as pd

df = pd.read_csv('name-age.csv')

print(df)

u_name = df['Name'].nunique()
print(f'Unique names: {u_name}')

u_age = df['Age'].nunique()
print(f'Unique ages: {u_age}')
























