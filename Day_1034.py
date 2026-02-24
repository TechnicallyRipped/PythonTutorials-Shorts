
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects

x = [1,2,3,4]
y = [1,2,3,4]

line, = plt.plot(x,y,color='green',
                 linewidth=4)

line.set_path_effects([
    path_effects.SimpleLineShadow(offset=(0, -5),
                                  shadow_color='red', 
                                  alpha=0.5),
    path_effects.Normal()])

plt.show()
