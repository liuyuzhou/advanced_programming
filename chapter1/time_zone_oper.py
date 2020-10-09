from datetime import datetime
from pytz import timezone
date_time = datetime(2020, 4, 28, 9, 30, 0)
print(f'current is: {date_time}')

central = timezone('US/Central')
chicage_date = central.localize(date_time)
print(f'chicage date is: {chicage_date}')


chine_d = chicage_date.astimezone(timezone('Asia/Shanghai'))
print(f'chine date is: {chine_d}')


from datetime import timedelta
import pytz
utc_d = chicage_date.astimezone(pytz.utc)
print(f'utc_d is: {utc_d}')


later_utc = utc_d + timedelta(minutes=30)
print(f'later_utc astimezone is: {later_utc.astimezone(central)}')


print(f"country timezone is:{pytz.country_timezones['CN']}")
