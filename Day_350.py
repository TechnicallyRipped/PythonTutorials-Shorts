

# pip install datefinder

import datefinder

x = '''Today's date is 3/26. A year ago
    the date was 3/26/23'''

dates_ = datefinder.find_dates(x)

# print(dates_)

for date in dates_:
    print(date)

















