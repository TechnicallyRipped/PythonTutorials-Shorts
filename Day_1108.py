

import sqlite3 as sql3

conn = sql3.connect('sales_data.db')

cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM raw_sales")

row_count = cursor.fetchone()[0]

print(row_count)

conn.close()
