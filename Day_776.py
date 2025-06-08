

from datetime import date, timedelta

def business_days(start_date, end_date):
    day_count = 0
    current = start_date
    while current < end_date:
        if current.weekday() < 5:  # 0=Mon, 6=Sun
            day_count += 1
        current += timedelta(days=1)
    return day_count

start = date(2025, 6, 7)
end = date(2025, 6, 22)

print(business_days(start, end)) 