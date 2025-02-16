


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Time to commute
week_1 = [20,25,22,45,30]
week_2 = [17,23,21,28,40]
week_3 = [21,26,22,40,36]
week_4 = [22,23,25,35,33]

data = np.array([week_1,week_2,week_3,week_4])

sns.heatmap(data, cmap='coolwarm')
plt.show()






























