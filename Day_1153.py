

import pandas as pd

df = pd.read_csv('ids.csv')

df['IdNum'] = (
    df['IdNum']
    .astype('str')
    .str.pad(width=6,
             side='left',
             fillchar='0')
)
print(df)













