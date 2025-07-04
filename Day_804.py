

import numpy as np

df = np.loadtxt('nums.csv', 
                  delimiter=',',
                  skiprows=1)

print(df)
