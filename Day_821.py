

import plotly.express as px

x_vals = [1, 2, 3, 4, 5]
y_vals = [10, 20, 15, 30, 25]

fig = px.scatter(x = x_vals,
                 y = y_vals,
                 range_x=[-2, 8],
                 range_y=[0, 50])

fig.update_traces(marker={'size':20})

fig.show()
