

# pip install seaborn
# pip install pandas
# pip install matplotlib

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('sb.csv')

sns.lineplot(data=df,x='A',y='B')

plt.show()
