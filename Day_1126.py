


import pandas as pd

df = pd.DataFrame({
    "Name": ["Joe", "Chris", "Tom", "Mike"],
    "Team": ["A", "B", "C", "D"]})


df2 = df[df["Team"].isin(["A", "C"])]

print(df2)


