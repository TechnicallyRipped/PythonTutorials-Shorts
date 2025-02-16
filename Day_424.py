



import pandas as pd

df = pd.read_csv('grades.csv')

# print(df)

extra_credit = ['Y','Y','Y','N','N']

df['Extra_Credit'] = extra_credit

print(df)




