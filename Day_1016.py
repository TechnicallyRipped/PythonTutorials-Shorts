

import pandas as pd

df = pd.read_csv('risks_.csv')

order = ['Low','Medium','High','Critical']

df['Risk'] = pd.Categorical(df['Risk'],
                            categories=order,
                            ordered=True)

df2 = df[df['Risk'] <= 'Medium']

print(df2)

