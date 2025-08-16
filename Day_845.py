


import numpy as np

x = np.array([[1, 2],
              [3, 4]])

flat_c = np.ravel(x, order='C')
print(flat_c)

flat_f = np.ravel(x, order='F')
print(flat_f)
