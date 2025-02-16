

# pip install pymysql
import pymysql

host = 'your_host' 
user = 'your_username'
password = 'your_password'
database = 'your_database'
connection = pymysql.connect(host=host, 
                             user=user, 
                             password=password, 
                             database=database)

cursor = connection.cursor()

cursor.execute("SELECT * FROM table_name")

rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
connection.close()








