



import polars as pl
import matplotlib.pyplot as plt

df = pl.read_csv('data.csv')

dates = list(df['Date'])
prices = list(df['Price'])

plt.plot(dates,prices)

plt.show()











