



import pandas as pd

df = pd.read_csv('null.csv')

styled_df = df.style.highlight_null(color='green')

print(styled_df)





























