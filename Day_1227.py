

import datefinder

text = '''
Today is October 26, 2026 .
Tomorrow is October 27th, 2026.'''

dates = datefinder.find_dates(text)

for date in dates:
    print(date.strftime("%B %d, %Y"))