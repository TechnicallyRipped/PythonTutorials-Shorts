

import pandas as pd

df = pd.DataFrame({
    'Name' :['Chris','Joe','Mike'],
    'T1' : [90,85,75],
    'T2' : [75,80,100]
})

df['Max_Score'] = df[['T1','T2']].max(axis=1)

print(df)

























