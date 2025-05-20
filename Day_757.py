

import pandas as pd

df = pd.DataFrame({
    'Name': ['Joe','John','Mike'],
    'Age': [30,33,31],
    'Score':[100,95,97]
})

df.to_csv('sep.csv',sep='||',
          index=False)
