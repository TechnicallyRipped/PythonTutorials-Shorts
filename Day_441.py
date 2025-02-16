

import matplotlib.pyplot as plt

x = [10, 20, 30, 40]
y = [1, 4, 9, 16]

plt.plot(x,y)

plt.tick_params(axis='x',direction='in', 
                length=40, width=5, color='blue')

plt.tick_params(axis='y',direction='inout', 
                length=5, width=2, color='red')
plt.show()
