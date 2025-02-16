

import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,20,30,40,50]

plt.bar(x, y, color='green')

for i, value in enumerate(y):
    plt.text(x[i], 0, str(value), ha='center', 
             fontsize=12, color='red')

plt.show()










