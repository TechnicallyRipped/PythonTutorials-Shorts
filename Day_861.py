
import duckdb

result = duckdb.query("""
SELECT * 
FROM read_csv_auto('df__1.csv')
                      
UNION 
                      
SELECT * 
FROM read_csv_auto('df__2.csv')                      
""").to_df()

print(result)
  













