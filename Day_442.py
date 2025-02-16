

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [5,5,15,20,25]

plt.plot(x, y)

plt.gca().invert_yaxis()
plt.gca().invert_xaxis()

plt.show()
