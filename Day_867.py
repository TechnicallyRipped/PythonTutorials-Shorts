
import duckdb

df = duckdb.query('''          
SELECT *
, SUM(Count) OVER (PARTITION BY State ORDER BY Date) AS Total
FROM read_csv_auto('st_having.csv')
ORDER BY State
''').to_df()

print(df)















# df = duckdb.query('''          
# SELECT *
# , SUM(Count) OVER (PARTITION BY State ORDER BY Date) AS Total
# FROM read_csv_auto('st_having.csv')
# ORDER BY State
# ''').to_df()

# print(df)


