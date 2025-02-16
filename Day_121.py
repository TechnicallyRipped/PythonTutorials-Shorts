



import yfinance as yf

stock = yf.Ticker('AAPL')

all_dividends = stock.dividends

all_dividends.to_csv('apple_dividends.csv')


























