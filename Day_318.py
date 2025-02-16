

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [2, 5, 7, 8, 3]
y2 = [4, 3, 8, 10, 6]


plt.plot(x, y1, color='red')

plt.gca().twinx()

plt.bar(x, y2, color='navy')

plt.show()

























