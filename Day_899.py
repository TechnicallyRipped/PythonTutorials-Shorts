
import matplotlib.pyplot as plt

x = ['Qtr 1 (Jan-March)',
     'Qtr 2 (April-June)',
     'Qtr 3 (July-Sept)',
     'Qtr 4 (Oct-Dec)']
y = [200,500,350,600]

plt.plot(x,y,color='blue')

plt.xticks(rotation=45)
plt.gcf().subplots_adjust(bottom=.4)

plt.show()