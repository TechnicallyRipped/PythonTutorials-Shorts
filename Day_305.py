

# pip install matplotlib

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [4, 2, 3, 6, 1]

plt.plot(x, y)

plt.grid(axis='x',color='red',linestyle=':')

plt.grid(axis='y',color='green',linestyle='--')

# plt.show()
plt.savefig('grids.png')











