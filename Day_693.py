
import pandas as pd
import sqlite3

my_db = sqlite3.connect('prods.db')

query = '''
SELECT 
    Region,
    sum(Sales) as Sales
FROM StateSales
GROUP BY Region
'''
df = pd.read_sql(query,my_db)
my_db.close()
print(df)