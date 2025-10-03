
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,4,10,8,6]

plt.plot(x, y, marker='o',color='blue')

for i, y_val in enumerate(y):
    plt.text(x[i],y_val+1,str(y_val),
             bbox=dict(boxstyle='square,pad=1',
                       facecolor='#fffb00',
                       edgecolor='#5f00d4',
                       linewidth=1,
                       alpha=0.7))

plt.show()
