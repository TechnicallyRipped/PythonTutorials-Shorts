

import duckdb

df = duckdb.query('''
SELECT *
FROM read_json_auto('ex.json')
''').to_df()

print(df)