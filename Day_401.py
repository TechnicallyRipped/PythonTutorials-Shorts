

import numpy as np


x = np.array([1,2,3,4,5,6,7,8])

# x_filter = (x > 4) & (x < 7)

# print(x_filter)

x2 = x[(x > 4) & (x < 7)]

print(x2)






