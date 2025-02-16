





import pandas as pd

df = pd.read_csv('output.csv')

df.rename(columns={'Name':'First_Name',
                   'Height':'Height(ft.)'}
                   , inplace=True)

print(df)

































