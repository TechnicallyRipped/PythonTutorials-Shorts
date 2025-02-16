

import matplotlib.pyplot as plt

x = [10, 20, 30, 40]
y = [1, 4, 9, 16]

plt.plot(x,y)

plt.gca().set_xticks([10, 20, 30, 40])
plt.gca().set_xticklabels(['ten', 'twenty', 
                           'thirty', 'forty'])

plt.gca().set_yticks([1, 4, 9, 16])
plt.gca().set_yticklabels(['one','two', 
                           'three','four'])

plt.show()
