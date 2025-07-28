
import plotly.graph_objects as go

values = [[20, 30, 35, 40, 17],
          [25, 28, 32, 22, 19],
          [20, 24, 20, 25, 20],
          [15, 22, 28, 17, 18]]
x_labels = ['Monday','Tuesday','Wednesday',
            'Thursday','Friday']
y_labels = ['Week 1','Week 2',
            'Week 3', 'Week 4']

fig = go.Figure(go.Heatmap(
    x=x_labels,
    y=y_labels,
    z=values,
    colorscale='Reds'))

fig.show()
