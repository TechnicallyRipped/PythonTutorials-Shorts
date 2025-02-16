

import pandas as pd

df = pd.read_csv('apply_ex.csv')

# print(df)

def classify_age(x):
    if x < 10:
        return 'Kid'
    elif x < 20:
        return 'Teenager'
    else:
        return 'Adult'

df['Age_Class'] = df['Age'].apply(classify_age)
print(df)




