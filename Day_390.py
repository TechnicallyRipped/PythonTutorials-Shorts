

import matplotlib.pyplot as plt

x = ['A', 'B', 'C', 'D', 'E']
y1 = [20, 35, 30, 35, 27]
y2 = [25, 32, 34, 20, 25]
y3 = [10, 12, 20, 22, 18]

plt.bar(x, y1)

plt.bar(x, y2, bottom=y1)

plt.bar(x, y3, 
        bottom=[y1[i] + y2[i] for i in range(len(y1))])

plt.show()
