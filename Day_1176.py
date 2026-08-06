


import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7]

y1 = [3, 4, 2, 5, 4, 6, 5]
y2 = [2, 1, 3, 2, 3, 2, 4]
y3 = [1, 2, 2, 1, 2, 3, 2]


plt.stackplot(x,y1,y2,y3,
              labels=["Apples", 
                      "Bananas",
                      "Oranges"])

plt.legend(loc="upper left")

plt.show()