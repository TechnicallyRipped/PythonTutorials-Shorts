
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe

x = [1,2,3,4]
y = [1,2,3,4]

line, = plt.plot(x,y,color='green',
                 linewidth = 5)

line.set_path_effects([
    pe.Stroke(linewidth=10, foreground='black'),
    pe.Normal()
])

plt.show()