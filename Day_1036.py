

import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [1,2,3,4]


for i in plt.style.available:
    print(i)

plt.style.use('dark_background')
# plt.style.use('ggplot')

plt.plot(x,y,linewidth = 5)

plt.show()








