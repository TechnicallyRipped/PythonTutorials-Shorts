

import pandas as pd

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Height": [165, 180, 175]
})

result = df[df.columns.difference(["Height"])]
print(result)
