


import pandas as pd

df = pd.read_csv('threeMonthSales.csv')

# print(df)

monthly = df.groupby('Month',
                     as_index=False).agg(
    TOTAL_SALES = ('Sales','sum'))

print(monthly)