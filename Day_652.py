

import sqlite3

conn = sqlite3.connect("new_db.db")
cursor = conn.cursor()

# cursor.execute("DELETE FROM table1 WHERE name = ?", ('Joe',))
# conn.commit()

pulled_data = cursor.execute("SELECT * FROM table1")
for row in pulled_data:
    print(row)

conn.close()













