

import matplotlib.pyplot as plt

x = [10, 20, 30, 40]
y = [1, 4, 9, 16]

plt.plot(x,y)

plt.tick_params(axis='x', labelsize=14, labelcolor='red')
plt.tick_params(axis='y', labelsize=4, labelcolor='green')

plt.show()
