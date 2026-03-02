

import pandas as pd

df = pd.read_csv('sale_group.csv')
df['Day'] = pd.to_datetime(df['Day'])

# print(df)

monthly_totals = df.groupby(
    pd.Grouper(key="Day", 
               freq="M"))["Sales"].sum()

print(monthly_totals)
