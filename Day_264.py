


import pandas as pd

df = pd.read_csv('grades.csv')

# print(df)
# print(df.dtypes)

df['Grade'] = df['Grade'].astype(int)

print(df)
print(df.dtypes)


#  .astype(str)
#  .astype(bool)
#  .astype(float)
#  .astype('datetime64[ns]')



















