

import pandas as pd

df = pd.DataFrame({"A": [1]})

x = df.squeeze()
print(x)
print(type(x))

