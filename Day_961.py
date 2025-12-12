

import pandas as pd

df = pd.read_csv('music.csv')

top_artists = (
    df.groupby(['artist_name'])
    .agg(plays=("artist_name", "count"))
      .sort_values("plays", ascending=False)
      .head(5)
)
print(top_artists)