

import pandas as pd

df = pd.read_csv('risks.csv')

order = ['Low','Medium','High']

df['Risk'] = pd.Categorical(df['Risk'],
                            categories=order,
                            ordered=True)

df['Risk_Level'] = df['Risk'].cat.codes

print(df)
