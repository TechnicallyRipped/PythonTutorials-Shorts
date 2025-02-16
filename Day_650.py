

import sqlite3

conn = sqlite3.connect("new_db.db")
cursor = conn.cursor()

# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS table1 (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         age INTEGER)''')

# data = [("John", 25),("Joe", 30)]

# cursor.executemany('''INSERT INTO table1 (name, age) 
#                    VALUES (?, ?)''', data)

# conn.commit()

pulled_data = cursor.execute("SELECT * FROM table1")
for row in pulled_data:
    print(row)
conn.close()

