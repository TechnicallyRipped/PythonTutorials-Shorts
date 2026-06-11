


import pandas as pd

df = pd.read_csv('random.csv')

x = df.sample(3,random_state=10)

print(x)