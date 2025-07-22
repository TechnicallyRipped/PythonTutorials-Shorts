
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.DataFrame({
    'Date': pd.date_range(start='2025-07-01', periods=12),
    'Price': [100, 102, 101, 105, 107, 110,
              113, 117, 120, 122, 121, 125,]})
df['MA_3'] = df['Price'].rolling(window=3).mean()

fig = px.line(df, x='Date', y='Price')
fig.add_trace(go.Scatter(
    x=df['Date'], y=df['MA_3'],
    mode='lines', name='3-Day MA',
    line={'color':'yellow'}))

fig.show()
