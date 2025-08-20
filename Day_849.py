

import pandas as pd

df = pd.DataFrame({
    "Test_Score": [65, 70, 75, 80, 85],
    "Hours_Studied": [1, 2, 3, 4, 5],
    "Hours_Gaming": [10, 9, 8, 7, 6]
})

print(df.corr())