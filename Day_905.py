



import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

x = [1, 2, 3, 4, 5]
y = [0, 12, 5, 18, 45]

plt.plot(x, y, marker='o')

plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=10))

plt.show()





