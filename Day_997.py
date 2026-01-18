
import pandas as pd
import mplfinance as mpf

df = pd.read_csv('goog.csv')

df["Date"] = pd.to_datetime(df["Date"])
df.set_index("Date", inplace=True)

mpf.plot(
    df,
    type="candle",
    title="Candlestick Chart",
    style="yahoo"
)
