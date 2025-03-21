
import pandas as pd
import sqlite3

my_db = sqlite3.connect('sales.db')

query = '''
SELECT * FROM LargeSales

UNION

SELECT * FROM SmallSales
'''

df = pd.read_sql(query,my_db)
print(df)
my_db.close()