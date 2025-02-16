
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10, 5, 7, 8, 3]

plt.plot(x, y)

plt.text(transform=plt.gca().transAxes,x=.1,y=.05, 
         s='TechnicallyRipped', alpha=0.5, rotation=35, 
         fontsize=40, color='gray',
         )

plt.show()















