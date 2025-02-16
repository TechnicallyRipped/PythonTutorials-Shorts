

import pandas as pd

df = pd.read_csv('col_count.csv')

# print(df)


country_count = df.value_counts(['Country','Vote'])
print(country_count)

