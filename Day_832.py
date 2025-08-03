

import plotly.express as px

years = [2022,2023,2024,2025]
expenses = [30,50,75,60]

fig = px.bar(x=years,y=expenses)

fig.update_layout(yaxis={'autorange':'reversed'})

fig.show()











