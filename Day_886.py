
import pandas as pd

df = pd.read_csv('threeMonthSales.csv')

x = df.groupby(['Product']).agg(
    Total_Sales = ('Sales','sum'),
    Avg_Sales = ('Sales','mean'),
    Min_Sales = ('Sales','min')
)

print(x)