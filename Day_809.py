
# pip install plotly

import plotly.express as px

items = ['Laptop','Phone','Camera','TV']
sales = [700, 300, 250, 500]

fig = px.bar(x=items, 
             y=sales,
             title='Sales by Item',
             labels={'x':'Item','y':'Sales'})

fig.show()
