

import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor

x = [1,2,3,4,5]
y = [10, 5, 7, 8, 3]

plt.plot(x, y)

cursor = Cursor(ax=plt.gca(), horizOn=True,
                vertOn=False, color='red')

plt.show()
