

import duckdb

df = duckdb.query('''          
SELECT *
FROM read_parquet('pTest.parquet')
''').to_df()

print(df)