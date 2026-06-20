

import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'Name': ['Joe','Kyle','Chris'],
    'Age' : [30,32,31],
    'Score': [90,85,95],
})

fig, ax = plt.subplots()

ax.axis('off')
ax.table(
    cellText=df.values,
    colLabels=df.columns,
    cellLoc='center',
    loc='center'
)

plt.show()