
import duckdb

df = duckdb.query('''          
SELECT *
FROM read_csv_auto('large_csv.csv')
LIMIT 10
''').to_df()

print(df)



