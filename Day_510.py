
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

np.random.seed(510)
data = np.random.rand(10, 10)

# (value, color)
colors = [(0, 'blue'), (0.5, 'white'),
          (0.75, 'yellow'), (1, 'red')]  
cust_cmap = LinearSegmentedColormap.from_list('custom_cmap', colors)

plt.imshow(data, cmap=cust_cmap)

plt.colorbar()

plt.show()
