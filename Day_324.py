

# pip install yahoo_fin
from yahoo_fin import options

ticker = 'AAPL'
strike_date = '2024-03-15'

stock_options = options.get_options_chain(ticker,
                                         date=strike_date)

calls = stock_options['calls']
puts = stock_options['puts']

calls.to_csv(f'{ticker}calls.csv',index=False)
puts.to_csv(f'{ticker}_puts.csv',index=False)













