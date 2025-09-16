

import duckdb

df = duckdb.query('''          
SELECT
  a.Name
, a.Score
, b.Age
FROM read_xlsx('scores_.xlsx', sheet='Sheet1') a
JOIN read_xlsx('scores_.xlsx', sheet='Sheet2') b
  ON a.Name = b.Name
''').to_df()

print(df)