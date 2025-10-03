

import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y1 = [2,4,5,7,10]
y2 = [30,20,15,19,10]

fig, ax = plt.subplots()

ax.plot(x, y1, color='blue')

ax2 = ax.twinx()
ax2.plot(x, y2, color='red')

plt.show()
