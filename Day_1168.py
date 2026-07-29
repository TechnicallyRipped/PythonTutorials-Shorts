


import pandas as pd

df = pd.read_csv('accounts.csv')

df['ID2'] = (
    df['ID'].str[:-3].str.replace('.','*',regex=True)
    + df['ID'].str[-3:]

)

print(df)

