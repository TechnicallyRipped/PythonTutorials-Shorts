


from datetime import datetime, timedelta

date = datetime.strptime('2024-01-01', '%Y-%m-%d')

new_date = date + timedelta(days=1,
                            seconds=1,
                            microseconds=1,
                            milliseconds=1,
                            minutes=1,
                            hours=1,
                            weeks=1)

print(date)
print(new_date)

