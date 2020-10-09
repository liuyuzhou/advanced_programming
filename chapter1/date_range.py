from datetime import datetime, date, timedelta
import calendar

def get_month_range(start_date=None):
    if start_date is None:
        start_date = date.today().replace(day=1)
    _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    end_date = start_date + timedelta(days=days_in_month)
    return start_date, end_date


a_day = timedelta(days=1)
first_day, last_day = get_month_range()
while first_day < last_day:
    print(f'first_day is: {first_day}')
    first_day += a_day


def date_range(start, stop, step):
    while start < stop:
        yield start
        start += step


for d in date_range(datetime(2020, 4, 1), datetime(2020, 5, 1), timedelta(hours=6)):
    print(f'range date is: {d}')