

import pandas as pd
import sqlite3

query = '''SELECT * FROM StateSales'''

with sqlite3.connect('prods.db') as my_db:
    df = pd.read_sql(query,my_db)

print(df)







