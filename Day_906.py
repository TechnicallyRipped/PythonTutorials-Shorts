

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

x = [1,2,3,4,5]
y = [800,1200,400,2000,1000]

def format_thousands(value, position):
    if value >= 1000:
        return(f"{round(value/1000,1)}K")
    else:
        return(value)

plt.plot(x, y)
plt.gca().yaxis.set_major_formatter(FuncFormatter(format_thousands))

plt.show()
