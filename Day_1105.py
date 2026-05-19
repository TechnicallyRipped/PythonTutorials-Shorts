

import sqlite3 as sql3
import pandas as pd

conn = sql3.connect('sales_data.db')

query = """SELECT * FROM raw_sales"""

df = pd.read_sql(query, conn)

print(df)

conn.close()