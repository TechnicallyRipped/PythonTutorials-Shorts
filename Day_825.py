
import plotly.express as px

cats = ['A','A','A','A','B','B','B','B',]
vals = [20,30,40,10,40,10,40,50]
years = [2020,2021,2022,2023,
         2020,2021,2022,2023]

fig = px.bar(x=cats,y=vals,
             color=cats,
             range_y=[0, 60],
             animation_frame=years,
             title='Slow Animation')

fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 2000
fig.layout.updatemenus[0].buttons[0].args[1]["transition"]["duration"] = 5000

fig.show()
