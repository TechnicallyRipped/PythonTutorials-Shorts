

import matplotlib.pyplot as plt

x = [1,2,3,4]
y1 = [1,2,3,4]
y2 = [4,3,2,1]

plt.plot(x,y1,color='red',linewidth=20,
         zorder=1)
plt.plot(x,y2,color='green',linewidth=20,
         zorder=0)

plt.show()



