
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
cursor.execute("SELECT * FROM scores")
cursor.close()
connection.close()

# print(cursor.description)
columns = [column[0] for column in cursor.description]

print(columns)






