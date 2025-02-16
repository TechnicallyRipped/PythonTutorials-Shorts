







import matplotlib.pyplot as plt

stocks = ['SPY', 'QQQ', 'VTI']
value = [3000, 2000, 500]

plt.pie(value, labels=stocks, autopct='%1.2f%%'
        , startangle=90) 

plt.title('Stock Portfolio')
plt.show()

























