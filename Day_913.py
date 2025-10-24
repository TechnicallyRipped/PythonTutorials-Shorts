

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]

apples = [3, 4, 2, 5, 4]
bananas = [1, 2, 3, 2, 1]
grapes = [2, 1, 2, 1, 2]

plt.stackplot(x, 
              apples, bananas, grapes, 
              labels=['Apples', 'Bananas', 'Grapes'],
              colors=['red','yellow','green'])

plt.legend(loc='upper right')

plt.show()
