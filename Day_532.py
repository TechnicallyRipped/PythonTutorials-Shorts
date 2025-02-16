

import pandas as pd

names = ['John','Danny','Chris']
scores = [[90,100,95],[95,94,93],[98,99,97]]

df = pd.DataFrame({'name':names,
                   'scores':scores})

print(df)

df2 = df.explode(['scores','iqs'])
print(df2)







