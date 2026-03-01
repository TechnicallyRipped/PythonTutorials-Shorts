

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

x = [1,2,3,4,5]
y = [1,2,3,4,5]

plt.plot(x,y)

logo = mpimg.imread('tr_logo.png')

imagebox = OffsetImage(logo, alpha=0.4) 

ab = AnnotationBbox(imagebox, (0.5, 0.5),
                    xycoords='axes fraction',
                    frameon=False)

plt.gca().add_artist(ab)

plt.show()