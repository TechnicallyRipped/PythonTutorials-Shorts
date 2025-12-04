

import pandas as pd

df = pd.DataFrame({
    'A':[1,2,3],
    'B':[100,200,300],
    'C':[100_000,200_000,300_000]})

df[df.select_dtypes(include="integer").columns] = (
    df.select_dtypes(include="integer")
      .apply(pd.to_numeric, downcast="integer"))

print(df.dtypes)
print(df.memory_usage(deep=True).sum())