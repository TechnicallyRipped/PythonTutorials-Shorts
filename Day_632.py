


# pip install fredapi

import pandas as pd
from fredapi import Fred

with open('f_api.txt') as file:
    key = file.read()

fred = Fred(api_key=key)

cpi_data = fred.get_series('CPIAUCSL')

df = pd.DataFrame(cpi_data,columns=['CPI'])
df.index.name = 'Date'
df.reset_index(inplace=True)

print(df)





















# cpi_df = pd.DataFrame(cpi_data, columns=['CPI'])
# cpi_df.index.name = 'Date'
# cpi_df.reset_index(inplace=True)