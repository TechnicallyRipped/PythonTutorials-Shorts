
import duckdb

con = duckdb.connect()

con.execute("""
    CREATE TABLE MY_TABLE AS
    SELECT * FROM read_csv_auto('df__1.csv');
""")

db_query = "SELECT * FROM MY_TABLE"

df = con.execute(db_query).fetchdf()

print(df)
