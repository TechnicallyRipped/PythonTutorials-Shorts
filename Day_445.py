

import matplotlib.pyplot as plt

x = [i for i in range(10)]
y = [i**2 for i in x]

plt.plot(x, y,color='red')
plt.plot(x, y,color='blue',drawstyle='steps-pre')
plt.plot(x, y,color='green',drawstyle='steps-post')

plt.show()
