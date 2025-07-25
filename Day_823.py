
import plotly.express as px

x=[0, 5, 10, 15, 20]
y=[1, 2, 3, 4, 5]

fig = px.line(x=x,y=y,
              markers=True)

fig.update_layout(xaxis={'tickvals':[0,10,20],
                         'ticktext':['Zero',
                                     'Ten',
                                     'Twenty']})

fig.show()
