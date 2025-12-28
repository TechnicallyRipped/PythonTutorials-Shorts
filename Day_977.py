

import pandas as pd

x = pd.Series([0,None,10])

x2 = x.dropna()
print(x2)

