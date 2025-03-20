
import pandas as pd
import sqlite3

my_db = sqlite3.connect('prods.db')

query = '''
SELECT *
FROM StateSales
ORDER BY Sales DESC
LIMIT 3; 
'''
df = pd.read_sql(query,my_db)
print(df)

my_db.close()