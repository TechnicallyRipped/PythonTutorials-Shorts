

import matplotlib.pyplot as plt
import numpy as np # Optional

np.random.seed(508) # Optional

x = np.random.randn(100)
y = np.random.randn(100)

plt.hexbin(x, y, gridsize=10, cmap='Blues',
           edgecolors='grey')

plt.colorbar()

plt.show()
