

import numpy as np

x = np.array([88,100,54,71,110])

conditions = [(x < 65),
              (x >= 65) & (x < 100),
              (x == 100)]

outcomes = ['Fail',
            'Pass',
            'Perfect Score']

result = np.select(conditions, 
                   outcomes, 
                   default='Unknown')

print(result)