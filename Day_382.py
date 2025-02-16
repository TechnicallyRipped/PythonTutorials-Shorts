

import matplotlib.pyplot as plt
import matplotlib.patches as patches

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x,y)

rectangle = patches.Rectangle((2,3),4,2, edgecolor='red',
                              facecolor='yellow')
plt.gca().add_patch(rectangle)

plt.show()











