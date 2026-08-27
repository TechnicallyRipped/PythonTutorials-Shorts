


import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 3, 7, 5]

plt.plot(x, y)

plt.show()




import plotly.express as px

x = [1, 2, 3, 4, 5]
y = [2, 4, 3, 7, 5]

fig = px.line(x=x, y=y)
fig.show()