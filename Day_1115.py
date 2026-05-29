

import pandas as pd

df = pd.DataFrame({
    "Name": ["John", "John", "Amy", "Amy"],
    "State": ["NY", "NY", "CA", "CA"],
    "Category": ["A", "B","A","B"],
    "Sales": [100, 200, 300, 400],
    "Profit": [10, 20, 30, 40]
})

result = df.groupby(["Name", "State"]).sum(numeric_only=True)

print(result)