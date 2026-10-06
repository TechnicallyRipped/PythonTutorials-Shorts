

import plotly.graph_objects as go

values = [30, 20, 50]
labels = ["A", "B", "C"]

fig = go.Figure(
    go.Pie(
        values=values,
        labels=labels,
        hole=.3
    )
)

fig.show()