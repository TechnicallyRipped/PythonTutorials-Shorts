
# pip install pandas
# pip install sqlalchemy
# pip install pymysql

import pandas as pd
from sqlalchemy import create_engine

host = 'your_host' 
user = 'your_username'
pwd = 'your_password'
db = 'your_database'

con_ = f'mysql+pymysql://{user}:{pwd}@{host}/{db}'

engine = create_engine(con_)
query = "SELECT * FROM scores;"

df = pd.read_sql(query, con=engine)

print(df)











