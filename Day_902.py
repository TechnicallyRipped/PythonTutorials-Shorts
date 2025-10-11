

import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,4,6,8,10]
y2 = [6,1,4,10,5]

line_style = dict(marker='o', 
                  color='red',
                  linewidth=2, 
                  linestyle="--")

plt.plot(x,y,**line_style)
plt.plot(x,y2,**line_style)

plt.show()





