
import plotly.express as px

x_vals = [1,2,3,4,5,1,2,3,4,5]
y_vals = [5,4,8,9,2,2,3,1,4,6]
category = ['A','A','A','A','A',
            'B','B','B','B','B']

fig = px.area(x=x_vals,
              y=y_vals,
              color=category,
              title='Ex: Area Plot')

fig.show()
