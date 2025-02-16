
import pandas as pd
import sqlite3

# df = pd.read_csv('df_1.csv')
# print(df)

conn = sqlite3.connect('data.db')

# df.to_sql('pandas', conn,
#           if_exists='replace',
#           index=False)
cursor = conn.cursor()
pulled_data = cursor.execute("SELECT * FROM pandas")
for row in pulled_data:
    print(row)
conn.close()

