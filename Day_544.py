
# pip install plotly
import matplotlib.pyplot as plt
import plotly.tools as tools

x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 17, 19]

plt.plot(x, y)

# plt.show()

plotly_fig = tools.mpl_to_plotly(plt.gcf())

plotly_fig.write_html('plot.html')

