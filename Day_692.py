
import pandas as pd
import sqlite3

my_db = sqlite3.connect('new_db.db')

query = '''
SELECT
    id,
    name as First_Name,
    age
FROM table1
'''

df = pd.read_sql(query,my_db)
my_db.close()
print(df)