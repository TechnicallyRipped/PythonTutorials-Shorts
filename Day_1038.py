
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe

x = [1,2,3,4,5,6]
y = [1,2,3,4,5,6]

plt.style.use("dark_background")

line, = plt.plot(x, y, color="#F2FF00",
                 linewidth=2)

line.set_path_effects([
    pe.Stroke(linewidth=10, 
              foreground="#F2FF00F5",
              alpha=0.3),
    pe.Stroke(linewidth=6, 
              foreground="#F2FF00E6", 
              alpha=0.5),
    pe.Normal()
])

plt.show()