from datetime import timedelta
a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
print(a)
c = a + b
print(f'{a} + {b} = {c}')
print(f'c.days = {c.days}')
print(f'c.seconds = {c.seconds}')
print(f'c.seconds / 3600 = {c.seconds / 3600}')
print(f'c.total_seconds() / 3600 = {c.total_seconds() / 3600}')


from datetime import datetime
a = datetime(2020, 1, 1)
print(f'{a} + timedelta(days=10) = {a + timedelta(days=10)}')
b = datetime(2020, 4, 28)
d = b - a
print(f'{b} - {a} = {b - a}')
print(f'd.days = {d.days}')
now_date = datetime.today()
print(f'the date time of now is: {now_date}')
print(f'{now_date} + timedelta(minutes=30) = {now_date + timedelta(minutes=30)}')


a = datetime(2019, 3, 1)
b = datetime(2019, 2, 28)
print(f'{a} - {b} = {a - b}')
print(f'{a} - {b} days = {(a - b).days}')

c = datetime(2020, 3, 1)
d = datetime(2020, 2, 28)
print(f'{c} - {d} days = {(c - d).days}')


a = datetime(2020, 4, 28)
# print(a + timedelta(months=1))

from dateutil.relativedelta import relativedelta
print(f'{a} + relativedelta(months=+1) = {a + relativedelta(months=+1)}')
print(f'{a} + relativedelta(months=+4) = {a + relativedelta(months=+4)}')
b = datetime(2020, 6, 10)
d = b - a
print(f'{b} - {a} = {b - a}')
d = relativedelta(b, a)
print(f'relativedelta(b, a) = {d}')
print(f'd.months = {d.months}')
print(f'd.days = {d.days}')
