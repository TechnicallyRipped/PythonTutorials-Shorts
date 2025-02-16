

import pandas as pd

df = pd.read_csv('df.csv')

print(df)

html_df = df.to_html()

with open("output.html", "w") as file:
    file.write(html_df)
