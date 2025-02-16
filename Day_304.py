

# pip install matplotlib

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [4, 2, 3, 6, 1]

plt.plot(x, y)

plt.gcf().set_facecolor('lightgreen')

plt.gca().set_facecolor('lightyellow')

plt.title('Change Colors')

plt.show()












