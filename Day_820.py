

import plotly.express as px

product = ['TV','Phone','Radio','Computer']
sales = [100, 130, 150, 170] 

fig = px.bar(x=sales, 
             y=product, 
             title='Horizontal Bar Chart',
             orientation='h')
fig.show()
