

import pandas as pd

df = pd.read_csv('bool.csv')

t = {'Yes':True,'No':False}

df['TF'] = df['Took_Exam'].map(t)

print(df)
print(df.dtypes)