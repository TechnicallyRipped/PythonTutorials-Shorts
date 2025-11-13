

import numpy as np

x = np.array([[1], 
              [2]])

y = np.array([[3],
              [4]])

result = np.hstack([x,y])
print(result)