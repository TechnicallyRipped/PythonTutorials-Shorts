


# pip install pyarrow
import pandas as pd

df = pd.read_parquet('df_1.parquet')

print(df)

# df.to_parquet('df_1.parquet',
#               engine='pyarrow')






