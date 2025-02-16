

import numpy as np

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

z = x @ y
print(z)

z2 = np.matmul(x,y)
print(z2)

