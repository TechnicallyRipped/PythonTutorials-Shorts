


import pandas as pd
import sidetable

df = pd.read_csv('null.csv')

print(df.stb.missing())
