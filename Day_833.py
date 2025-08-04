
import plotly.express as px

numbers = [100, 60, 45, 25, 15]

stage = ["Visitors","Signups",
         "Email Confirmed",
         "Free Trial Started",
         "Subscribed"]

fig = px.funnel(x=numbers, y=stage)

fig.show()