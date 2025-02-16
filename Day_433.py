


from datetime import datetime as dt

date1 = dt.strptime('2024-01-24', '%Y-%m-%d')
date2 = dt.strptime('2024-06-24', '%Y-%m-%d')

diff = date2 - date1
# print(diff)

day_diff = diff.days

print(day_diff)

