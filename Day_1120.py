

import pandas as pd

df = pd.DataFrame({
    "Start": ["2026-01-01","2026-01-01","2026-01-01"],
    "Duration": [1,2,3]})

df['Start'] = pd.to_datetime(df['Start'])

df['Duration'] = pd.to_timedelta(df['Duration'],
                                 unit='days')

df['End'] = df['Start'] + df['Duration']

print(df)
