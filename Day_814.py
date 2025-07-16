
import plotly.express as px

items = ['Laptop','Phone','Camera','TV']
sales = [700, 300, 250, 500]

fig = px.bar(x=items, 
             y=sales,
             title='Sales by Item',
             labels={'x':'Item','y':'Sales'})

fig.update_yaxes(title_font={'color':'hotpink',
                             'size':30,
                             'family':'monospace'})
fig.update_xaxes(title_font={'color':'limegreen',
                             'size':60,
                             'family':'fantasy'})

fig.show()













# 
# fig.update_xaxes(title_font={'color':'limegreen',
#                              'size':60,
#                               'family':'fantasy'})
