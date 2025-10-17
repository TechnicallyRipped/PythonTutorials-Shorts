

import pandas as pd

df = pd.read_csv('numbers.csv',
                 dtype={'Num1':'int8',
                        'Num2':'int8'})

print(df.describe())
print(df.info(memory_usage='deep'))