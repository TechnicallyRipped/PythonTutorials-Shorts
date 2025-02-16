

from datetime import datetime,timedelta

x = '2025271'

yr = int(x[:4])
d = int(x[4:])

# print(f'{yr=}, {d=}')

normal_date = datetime(yr,1,1) + timedelta(days=d-1)
print(normal_date)

