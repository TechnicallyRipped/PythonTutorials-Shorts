

import plotly.express as px
import pandas as pd

data = {
    "state": ["CA", "TX", "NY", "FL", "IL"],
    "value": [300, 250, 200, 220, 180]
}
df = pd.DataFrame(data)

fig = px.choropleth(
    df,
    locations="state",
    color="value",
    locationmode="USA-states",
    scope="usa"
)

fig.show()
