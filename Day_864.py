
import duckdb

df = duckdb.query('''          
SELECT * 
FROM read_csv_auto('df__1.csv')
WHERE Score >= 90
  AND Name = 'Nick'
''').to_df()

print(df)

