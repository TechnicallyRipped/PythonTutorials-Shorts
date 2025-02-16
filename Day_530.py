

# pip install pyjanitor

import pandas as pd
import janitor

df = pd.read_csv('col_space.csv')

df = df.clean_names(case_type="preserve")

print(df)












