

import pandas as pd

df1 = pd.DataFrame({
    'A': [1, 2],
    'B': [3, 4]
})

df2 = pd.DataFrame({
    'A': [10, 20],
    'C': [30, 40]
})

df1.update(df2)

print(df1)



