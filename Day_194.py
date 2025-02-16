



import matplotlib.pyplot as plt
import random


colors = [0,0,0]

for i in range(100):
    colors[random.randint(0,2)] += 1
    plt.bar(['Red','Blue','Green'],colors
            ,color=['red','blue','green'])
    plt.pause(0.1)
plt.show()




























