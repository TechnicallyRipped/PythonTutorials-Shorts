

# pip install matplotlib

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [4, 2, 3, 6, 1]
y2 = [3,1,6,3,2]

plt.plot(x, y1)
plt.plot(x, y2)

plt.legend(['~Y1~', '~Y2~'])

plt.show()




















