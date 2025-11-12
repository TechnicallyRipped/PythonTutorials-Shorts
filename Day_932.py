

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Score' : [70,70,90,95],
    'Honors' : ["N","Y","N","Y"]
})

conditions = [
    (df['Score'] >= 65) & (df['Honors'] == 'N'),
    (df['Score'] >= 75) & (df['Honors'] == 'Y'),
]

choices = ['P','P']

df['P_F'] = np.select(conditions, choices, default='F')
print(df)

























