

import os
import time

file_path = "data.csv"
creation_time = os.path.getctime(file_path)

readable_time = time.ctime(creation_time)
print(readable_time)