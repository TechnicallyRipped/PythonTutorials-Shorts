
import pandas as pd
import sqlite3

my_db = sqlite3.connect('prods.db')

query = '''
SELECT *
FROM StateSales
WHERE Region = 'NorthEast'
    AND State = 'New York'
'''

df = pd.read_sql(query,my_db)
my_db.close()
print(df)


