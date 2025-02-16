

import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]

plt.plot(x, y)

ax = plt.gca()

for spine in ax.spines.values():
    # spine.set_visible(False)
    spine.set_color('red')

plt.show()
