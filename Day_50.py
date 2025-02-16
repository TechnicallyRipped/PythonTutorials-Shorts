




import datetime


x = datetime.datetime.now()

print(x.strftime('%H:%M'))

time_change = datetime.timedelta(days=1)

x = x + time_change

print(x.strftime('%H:%M'))

















