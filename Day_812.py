
import plotly.express as px

x_vals = [1, 2, 3, 4, 5]
y_vals = [10, 15, 13, 17, 21]
categories = ['A', 'A', 'B', 'B', 'C']
s = [3, 6, 7, 2, 10]

fig = px.scatter(x=x_vals,
                 y=y_vals,
                 color=categories,
                 size=s,
                 title='My Scatter Plot')

fig.show()
