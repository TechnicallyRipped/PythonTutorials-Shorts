

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y)

plt.xticks(rotation=45)
plt.yticks(rotation=60)

plt.show()
