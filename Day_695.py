
import pandas as pd
import sqlite3

my_db = sqlite3.connect('prods.db')

query3 = '''
SELECT 
    a.*
    , b.AverageAge
FROM StateSales a
JOIN StateMetrics b
    ON a.State = b.State'''
df3 = pd.read_sql(query3,my_db)
print(df3)

my_db.close()