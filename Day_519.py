
import pandas as pd

date_range = pd.date_range(start='2023-01-01', 
                           end='2023-03-01', 
                           freq='M')

df = pd.DataFrame({'Date': date_range})

print(df)
#    'D': Day
#    'B': Business day
#    'W': Weekly
#    'M': Month-end
#    'H': Hourly
#    'T' or 'min': Minutes
#    'S': Seconds