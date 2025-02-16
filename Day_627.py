


import numpy as np

score = np.array([90,85,62,80,50])

pass_fail = np.where(score < 65,'Fail','Pass')

print(pass_fail)

