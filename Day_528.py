

import pandas as pd

df = pd.read_csv('replace_names.csv')

replacements = {'M':'Male','F':'Female'}

df['Gender'] = df['Gender'].replace(replacements)

print(df)








