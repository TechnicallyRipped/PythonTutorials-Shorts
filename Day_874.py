

import duckdb

df = duckdb.query('''          
SELECT *
FROM read_xlsx('scores_.xlsx', sheet='Sheet2')
''').to_df()

print(df)