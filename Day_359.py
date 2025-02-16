



import pandas as pd

df = pd.read_csv('large_df.csv', skiprows=99, 
                 nrows=100, header=None)

header = pd.read_csv('large_df.csv', nrows=0)

df.columns = list(header)

print(df)


















