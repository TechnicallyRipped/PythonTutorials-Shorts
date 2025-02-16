



import yfinance as yf
import matplotlib.pyplot as plt

data = yf.download("AAPL", start="2019-01-01", 
                   end="2023-07-14")
data = data.reset_index()
dates = list(data['Date'])
close = list(data['Close'])

plt.plot(dates, close)
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Apple Stock Price')
plt.show()



























