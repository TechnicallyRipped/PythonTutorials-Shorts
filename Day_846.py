

import numpy as np

x = np.array([10, 20, 30, 20, 40, 20])

y = np.where(x == 20)[0]

print(y)
