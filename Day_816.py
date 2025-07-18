

import plotly.express as px

items = ['Laptop','Phone','Camera']
sales = [700, 300, 250]

fig = px.bar(x=items, y=sales,color=items)

fig.update_layout(legend={'bgcolor':"lightblue",
                          'bordercolor':'red',
                          'borderwidth':10})

fig.show()



