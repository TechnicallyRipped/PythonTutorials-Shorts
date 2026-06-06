

import pandas as pd

df = pd.DataFrame({
    'col1' : ['A','B','C','D'],
    'col2' : [1,2,3,4],
    'col3' : ['a','b','c','d']
})

df['col3'] = df['col3'].iloc[::-1].values

print(df)







