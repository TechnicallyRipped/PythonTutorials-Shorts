

import pandas as pd

df = pd.DataFrame({
    "Team": ["B", "A", "C", "A", "B", "C", "A"],
    "Points": [15, 10, 30, 25, 20, 35, 18]
})

df['Team_Num'] = df.groupby(["Team"],
                            sort=False).ngroup()

print(df)
