


from datetime import datetime, date, time

my_date = date(2024, 5, 11)
my_time = time(12, 30, 0)

my_datetime = datetime.combine(my_date, my_time)

print(my_datetime)