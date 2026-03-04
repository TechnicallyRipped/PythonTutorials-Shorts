

import pandas as pd

df = pd.read_csv('setAxis.csv')

df = df.set_axis(['Name','Score'],axis=1)

print(df)