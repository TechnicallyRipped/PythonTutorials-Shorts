

# pip install plotly

import plotly.express as px
import pandas as pd

df = pd.read_csv('sb_ex.csv')

fig = px.sunburst(df, path=['Sector', 'Ticker'],
                  values='Value')

fig.show()
