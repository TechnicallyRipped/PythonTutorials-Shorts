

import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D', 'E']
values1 = [20, 35, 30, 35, 27]
values2 = [25, 32, 34, 20, 25]
values3 = [10, 12, 20, 22, 18]

plt.bar(categories, values1,
        label='Group 1')

plt.bar(categories, values2, bottom=values1,
        label='Group 2')

plt.legend()
plt.show()
