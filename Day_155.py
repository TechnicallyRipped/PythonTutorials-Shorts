


# pip install matplotlib
# pip install seaborn

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.lmplot(x="total_bill", y="tip", data=tips)
plt.show()






















