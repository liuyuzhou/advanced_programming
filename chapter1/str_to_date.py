from datetime import datetime
date_text = '2020-04-20'
y = datetime.strptime(date_text, '%Y-%m-%d')
z = datetime.now()
print(f'{z} - {y} = {z - y}')


print(f'z = {z}')
print(f"datetime.strftime(z, '%A %B %d, %Y') = {datetime.strftime(z, '%A %B %d, %Y')}")


from datetime import datetime
def parse_ymd(s):
    year_s, mon_s, day_s = s.split('-')
    return datetime(int(year_s), int(mon_s), int(day_s))
