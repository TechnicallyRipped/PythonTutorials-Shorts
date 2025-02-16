

# pip install matplotlib
# pip install matplotlib_venn

import matplotlib.pyplot as plt
from matplotlib_venn import venn2

x = {1, 2, 3, 4}
y = {3, 4, 5, 6}

venn2([x,y])

plt.show()







