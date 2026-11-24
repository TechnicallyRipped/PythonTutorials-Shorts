

import pandas as pd

df = pd.DataFrame({
    'Letter':['A','B','C'],
    'Price': [10.456, 20.789, 30.123]
})

df['Price'] = df['Price'].round(1)

print(df)