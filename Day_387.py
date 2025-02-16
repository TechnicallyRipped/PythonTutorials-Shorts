
import matplotlib.pyplot as plt
import matplotlib.patches as patches

x = [1,2,3,4,5]
y = [1,3,5,2,4]

plt.plot(x,y)

wedge = patches.Wedge((2, 2), r=1, theta1=0, theta2=75, 
                      edgecolor='red', facecolor='grey')
plt.gca().add_patch(wedge)

plt.show()













