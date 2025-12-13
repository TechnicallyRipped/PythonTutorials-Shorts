

import pandas as pd

df = pd.DataFrame({
    "team": ["A", "A", "A", "B", "B", "B"],
    "points": [10, None, None, 7, 5, None]
})

grouped_df = df.groupby("team").agg(
    total_rows=("points", "size"),
    total_sucess=("points","count")
)

print(grouped_df)