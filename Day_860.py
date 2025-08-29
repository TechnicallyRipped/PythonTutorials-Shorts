

import duckdb

result = duckdb.query("""
SELECT 
  State
, SUM(Revenue) as State_Revenue
FROM read_csv_auto('sales.csv')
GROUP BY State
""").to_df()

print(result)
  













