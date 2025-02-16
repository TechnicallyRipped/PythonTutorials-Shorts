


import pandas as pd
import sqlite3 

# my_db = sqlite3.connect('data.db')
# df = pd.read_sql("SELECT * FROM table1", my_db)
# my_db.close()

with sqlite3.connect('data.db') as my_db:
    df = pd.read_sql("SELECT * FROM table1", my_db)

print(df)




