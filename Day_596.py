
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [1, 2, 3, 4]
z = [0, 0, 0, 0]

dx = [1, 1, 1, 1]
dy = [1, 1, 1, 1]
dz = [1, 2, 3, 4]

ax = plt.figure().add_subplot(projection='3d')

ax.bar3d(x, y, z, dx, dy, dz, color='blue')

ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')

plt.show()