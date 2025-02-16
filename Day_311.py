

import matplotlib.pyplot as plt

day = ['1/1/24','1/2/24','1/3/24','1/4/24']

retail = [100,110,120,90]
cost = [90,92,107,87]

plt.plot(day, retail,color='blue',
         label='Retail Sales')
plt.plot(day, cost,color='red',
         label='Cost of Goods')

plt.fill_between(x=day, y1=retail, y2=cost,
                 color='green',alpha=.3)

plt.legend()
plt.show()











