

import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [0,4,5,2,3]

plt.plot(x, y)

plt.annotate(text='Text', 
             xy=(4, 2), xytext=(3, 1),
             arrowprops=dict(facecolor='red'))

plt.show()








