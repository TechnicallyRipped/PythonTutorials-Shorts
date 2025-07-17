

import plotly.express as px

items = ['Laptop','Phone','Camera']
sales = [700, 300, 250]

colors_ = ['cccc','rgb(0, 75, 255)',"#22ee0b"]

fig = px.bar(x=items, y=sales)

fig.update_traces(marker_color=colors_)

fig.show()










