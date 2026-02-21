

import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [1,2,3,4]

plt.plot(x,y)

plt.text(2,3,'Hello World!',
         fontsize=18,
         color='red',
         bbox=dict(facecolor="yellow",
                   edgecolor="green",
                   linewidth=2))

plt.show()



