

import polars as pl
import time

start = time.time()
df = pl.scan_csv('large_file.csv')

df = df.filter(pl.col('id') > 800000)

df = df.collect()

end = time.time()

print(f"Total time {round(end-start,4)} seconds")


