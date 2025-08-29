

import duckdb

result = duckdb.query("""
SELECT 
  a.ID
, a.Name
, b.Score
FROM read_csv_auto('j1.csv') a
JOIN read_csv_auto('j2.csv') b
  ON a.ID = b.ID""").to_df()

print(result)
print(type(result))
result.to_csv('my_joined_df.csv')













