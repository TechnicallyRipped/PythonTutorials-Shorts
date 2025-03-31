

import numpy as np

x = [1, 3]
y = [2, 10]

x_val = 5

y_val = np.interp(x_val, x, y)

print(y_val)