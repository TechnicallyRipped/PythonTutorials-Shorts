

import matplotlib.pyplot as plt
import matplotlib.patches as patches

x = [0, 1, 2, 3, 4]
y = [3, 2, 3, 1, 2]

plt.plot(x,y)

circle = patches.Circle((2,3),.25, edgecolor='green',
                              facecolor='pink')
plt.gca().add_patch(circle)


plt.show()











