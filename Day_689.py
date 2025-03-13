

import pandas as pd

df = pd.read_csv('date_df.csv',
                 parse_dates=['Date','Date2'])

print(df)
print(df.dtypes)








