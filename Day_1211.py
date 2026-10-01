


import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 3, 6, 5]

plt.plot(x, y)

plt.plot(3, 3,
         marker="o",
         markersize=10,
         markerfacecolor="yellow",
         markeredgecolor="green",
)

plt.show()