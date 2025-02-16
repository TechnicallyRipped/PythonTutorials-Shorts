

import csv
import matplotlib.pyplot as plt


with open('data.csv', 'r') as file:
    content = csv.reader(file) 

    date_ = []
    price = []
    next(content)
    
    for row in content:
        date_.append(row[0]) 
        price.append(float(row[1]))

plt.plot(date_, price)
plt.show()








































