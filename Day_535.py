

import pandas as pd

df = pd.read_csv('pass_fail.csv')

key,key_value = pd.factorize(df['Subject'])

df['encoded'] = key

print(df)
























