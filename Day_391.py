


import matplotlib.pyplot as plt

y = ['Category A', 'Category B', 'Category C']
x1 = [10, 15, 20]
x2 = [5, 10, 15]
x3 = [8, 12, 18]

plt.barh(y,x1)
plt.barh(y,x2,left=x1)
plt.barh(y,x3,left=[x1[i] + x2[i] for i in range(len(x1))])

plt.show()













