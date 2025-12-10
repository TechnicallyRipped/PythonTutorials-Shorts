


from datetime import datetime
from zoneinfo import ZoneInfo, available_timezones

location_ = ZoneInfo('America/Phoenix')

loc_time = datetime.now(location_)

print(loc_time)

print(available_timezones())