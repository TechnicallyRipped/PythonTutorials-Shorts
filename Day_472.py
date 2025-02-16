

import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [3,1,4,2,6]
errors = [.3,.4,.3,.6,.2]

plt.errorbar(x,y,yerr=errors,fmt='o')

plt.show()

