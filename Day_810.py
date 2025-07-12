

import plotly.express as px

labels = ['Laptop', 'Phone', 'Camera']
sales = [700, 300, 250]

fig = px.pie(names=labels,
             values=sales,
             title='My Pie Chart',
             hole=.35)

fig.show()
