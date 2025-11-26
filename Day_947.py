

import pandas as pd

df1 = pd.DataFrame({'id': [1, 2, 3], 
                    'A': ['a', 'b', 'c']})

df2 = pd.DataFrame({'id': [3, 4, 5],
                    'B': ['x', 'y', 'z']})

outer_df = df1.merge(df2,
                     on=['id'],
                     how='outer',
                     indicator=True)

print(outer_df)






