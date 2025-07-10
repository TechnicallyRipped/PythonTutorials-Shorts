

import pandas as pd
import plotly.express as px

df = pd.read_csv('aapl_30.csv')

fig = px.line(df , x='Date', y='Price',
              title="Apple Price")
fig.show()









