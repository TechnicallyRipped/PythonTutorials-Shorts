
import duckdb

df = duckdb.query('''
WITH daily_sales as(
    SELECT 
        Date
    , SUM(Sales) as DailySales
    FROM read_csv_auto('salesCTE.csv')
    GROUP BY Date
)
                  
SELECT * 
FROM daily_sales
''').to_df()

print(df)

