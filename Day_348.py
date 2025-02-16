
# pip install matplotlib
# pip install squarify

import matplotlib.pyplot as plt
import squarify

sizes = [3.1, 2.66, 2.35, 1.88, 1.85]
labels = ['MSFT','AAPL','NVDA','GOOG','AMZN']
colors = ['red','blue','green','yellow','purple']

squarify.plot(sizes=sizes, label=labels,
              color=colors,
              text_kwargs={'color':'white', 'fontsize':18})

plt.axis('off')

plt.show()




