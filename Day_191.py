



import matplotlib.pyplot as plt
import random

x = [random.randint(0,100) for i in range(100)]
y = [random.randint(0,100) for i in range(100)]
z = [random.randint(0,100) for i in range(100)]


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x, y, z)
plt.show()































