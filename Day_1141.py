



import pandas as pd

df = pd.DataFrame({
    "Color": ["Blue", "Red", "Red", 
              "Green", "Red", "Blue",]
})

counts = df["Color"].value_counts()
print(counts)

most_common = counts[counts == counts.max()]

print(most_common.index.to_list())
