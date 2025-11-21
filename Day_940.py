

import pandas as pd

df = pd.DataFrame({
    "ID": ["Order #1", "Order #456", "Order #9999"]
})

df["Order_Num"] = df["ID"].str.extract(r"#(\d+)")

print(df)
