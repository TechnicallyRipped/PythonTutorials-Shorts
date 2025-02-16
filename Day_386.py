

import matplotlib.pyplot as plt

l = ['A', 'B', 'C', 'D']
s = [15, 30, 45, 10]
e = (0,.1,0,0)

plt.pie(s, labels=l, explode=e,
        shadow=True)

plt.show()
