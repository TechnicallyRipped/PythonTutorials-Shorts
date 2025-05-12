

from datetime import datetime

time_24 = "18:45:00"  # 6:45 PM

time_obj = datetime.strptime(time_24, "%H:%M:%S").time()

# print(time_obj)

time_12 = time_obj.strftime("%I:%M:%S %p")

print(time_12)










