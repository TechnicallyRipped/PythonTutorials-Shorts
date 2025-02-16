

import matplotlib.pyplot as plt

x = [i for i in range(100)]
y1 = [i for i in range(100)]
y2 = [i**2 for i in range(100)]
y3 = [i%10 for i in range(100)]

plt.subplot(2, 2, 1)
plt.plot(x, y1)
plt.title('Y = X')

plt.subplot(2, 2, 2)
plt.plot(x, y2)
plt.title('Y = X^2')

plt.subplot(2, 2, 3)
plt.plot(x, y3)
plt.title('Y = X%10')

plt.tight_layout()
plt.show()


