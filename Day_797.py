
from scipy.stats import linregress
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8]
y = [2,5,4,6,9,8,7,10]

lin_re = linregress(x, y)
slope = lin_re.slope
intercept = lin_re.intercept

y2 = [slope*i+intercept for i in x]

plt.scatter(x,y,color='blue')
plt.plot(x,y2,color='red')
plt.show()








# lin_re = linregress(x, y)
# slope = lin_re.slope
# intercept = lin_re.intercept

# y2 = [slope*i+intercept for i in x]
# print(y2)

# plt.plot(x,y2,color='red')
# plt.show()



