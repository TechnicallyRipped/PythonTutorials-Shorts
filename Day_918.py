

import pandas as pd

df = pd.DataFrame({
    'Color' : ['Red', 'Blue', 'Green', 'Red'],
    'Count' : [10,20,30,40]
})

print(df)

dummies = pd.get_dummies(df, 
                         columns=['Color'],
                         dtype=int,
                         prefix='C')
print(dummies)







