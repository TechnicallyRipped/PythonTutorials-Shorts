

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [4, 2, 3, 6, 1]


plt.plot(x, y, color='red')

img = plt.imread('graph_bg.png')

plt.imshow(img, aspect='auto', 
           extent=[min(x), max(x), min(y), max(y)])

plt.show()
















