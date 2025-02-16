

# pip install duckdb
import duckdb
# import pandas as pd

# df = pd.read_csv('df.csv')

my_query = 'SELECT * FROM "df.csv" WHERE Grade > 95'

results = duckdb.query(my_query).to_df()

print(results)