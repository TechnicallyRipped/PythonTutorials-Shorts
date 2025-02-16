
import requests
import pandas as pd

url = "https://api.coingecko.com/api/v3/coins/ripple/market_chart"

params = {"vs_currency": "usd",
          "days": "365"}

response = requests.get(url, params=params)
data = response.json()

df = pd.DataFrame(data["prices"], columns=['Date','Price'])
df['Date'] = pd.to_datetime(df['Date'], unit="ms")

print(df)



 