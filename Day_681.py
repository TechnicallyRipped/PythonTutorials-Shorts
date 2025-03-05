


import pandas as pd

df = pd.read_csv('zipcodes.csv',
                 dtype={'Zip_Code':'string'})

print(df)
print(df.dtypes)






