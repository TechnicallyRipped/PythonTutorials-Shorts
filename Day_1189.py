


import matplotlib.pyplot as plt

data = {'A' : 10,
        'B' : 20, 
        'C' : 30}

plt.pie(x = data.values(),
        labels= data.keys())

plt.show()