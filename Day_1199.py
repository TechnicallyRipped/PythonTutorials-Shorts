

import pandas as pd

df = pd.DataFrame({
    'Name':['Joe','Mike','John'],
    'Score':[94,95,93]})

print(df)

df.to_clipboard()
