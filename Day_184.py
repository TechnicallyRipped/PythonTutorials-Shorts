

# pip install mplfinance
# pip install yfinance
 
import mplfinance as mpf
import yfinance as yf

stock_data = yf.download('AAPL' ,start='2023-06-01', 
                         end='2023-09-01')

mpf.plot(stock_data, type='candle', style='yahoo')

































