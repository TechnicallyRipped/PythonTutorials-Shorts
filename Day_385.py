
import matplotlib.pyplot as plt

labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]
colors = ['red', 'green', 'blue', 'yellow']
explode = (0, .8, 0, 0) 

plt.figure(figsize=(8, 6))
plt.pie(sizes, explode=explode, labels=labels, colors=colors)

plt.show()












