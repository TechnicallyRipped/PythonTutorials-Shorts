

import pandas as pd

df = pd.read_csv('car.csv')

df['PCT1'] = df['Raw_Rate'].map("{:.2%}".format)

df['PCT2'] = df['Percent'].map("{:.2f}%".format)

print(df)