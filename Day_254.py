

# pip install pymysql
import pymysql
import pandas as pd

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
rows = cursor.fetchall()
cursor.close()
connection.close()

columns = [column[0] for column in cursor.description]

df = pd.DataFrame(rows, columns=columns)
print(df)






