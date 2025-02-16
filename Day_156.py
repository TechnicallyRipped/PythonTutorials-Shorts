





import pandas as pd

df = pd.read_csv('grouping.csv')

group = df.groupby(['State', 'City'])

sum_state = group['People'].sum()

print(sum_state)






























