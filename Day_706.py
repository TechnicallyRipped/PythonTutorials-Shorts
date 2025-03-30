

import pandas as pd


df = pd.read_csv('numbers.csv')

df = df.assign(a=df['Num1']+df['Num2'],
               s=df['Num1']-df['Num2'],
               m=df['Num1']*df['Num2'])

print(df)

# df['a'] = df['Num1'] + df['Num2']
# df['s'] = df['Num1'] - df['Num2']
# df['m'] = df['Num1'] * df['Num2']



