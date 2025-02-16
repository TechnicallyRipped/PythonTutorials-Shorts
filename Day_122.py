



import yfinance as yf

stock = yf.Ticker('AAPL')

for data_point in stock.info:
    print(f'{data_point} ---- {stock.info[data_point]}')






















