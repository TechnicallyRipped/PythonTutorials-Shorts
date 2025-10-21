

import pandas as pd

df = pd.read_csv('MinMax.csv')

print(df)

def minMax(col:pd.Series):
    return col.max() - col.min()

df2 = df.groupby(['Region']).agg(
    Total_Sales = ('Sales','sum'),
    MinMax = ('Sales',minMax)
)

print(df2)


