

import pandas as pd

df = pd.read_csv('df.csv')

q_var = df['Grade'].mean()

df2 = df.query('Grade >= @q_var')
print(df2)
