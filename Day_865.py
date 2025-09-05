
import duckdb

df = duckdb.query('''          
SELECT
  State
, SUM(Count) as State_Count
FROM read_csv_auto('st_having.csv')
GROUP BY State
HAVING State_Count >= 20
''').to_df()

print(df)



