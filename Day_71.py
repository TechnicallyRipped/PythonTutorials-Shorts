

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot(x='Date', y='Price')

plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Date vs Price')

plt.show()

























