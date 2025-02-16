

import pandas as pd

df = pd.read_excel('skipCol.xlsx',
                   usecols='B:C',
                   skiprows=3,
                   nrows=2)

print(df)
















