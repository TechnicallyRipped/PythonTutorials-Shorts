

import matplotlib.pyplot as plt

x = [1,2,3,4]
y1 = [1,2,3,4]
y2 = [2,3,4,5]

plt.plot(x,y1,color='red',
         linewidth=5,
         linestyle='--')

plt.plot(x,y2,color='green',
         linewidth=5,
         dashes=[8,5])

plt.show()