

# pip install cryptocompare
import cryptocompare as cp

x = cp.get_historical_price_day('BTC',
                                currency='USD', 
                                limit=10)


for day in x:
    print(day['close'])



























