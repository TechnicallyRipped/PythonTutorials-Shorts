


import pandas as pd

df = pd.DataFrame(
    {"points": [10, 30, 20]},
    index=["b", "c", "a"]
)

df = df.sort_index(ascending=False)

print(df)