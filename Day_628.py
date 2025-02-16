


import numpy as np

x = np.array([1, 2, 3])

pad_x = np.pad(x,(2,1),constant_values=5)

print(pad_x)
