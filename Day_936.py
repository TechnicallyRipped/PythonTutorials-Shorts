

import pandas as pd
import numpy as np

df = pd.DataFrame({'Age':[24,50,80]})

df['AgeClass'] = np.where(
    df['Age'] >= 65, 'Senior',np.where(
        df['Age'] >= 30,'Adult','Young Adult'
))

print(df)
