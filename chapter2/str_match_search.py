text_val = 'life is short, I use python, what about you'
print(text_val == 'life')
print(text_val.startswith('life'))
print(text_val.endswith('what'))
print(text_val.find('python'))


date_text_1 = '04/20/2020'
date_text_2 = 'April 20, 2020'

import re
if re.match(r'\d+/\d+/\d+', date_text_1):
    print('yes,the date type is match')
else:
    print('no,it is not match')

if re.match(r'\d+/\d+/\d+', date_text_2):
    print('yes,it match')
else:
    print('no,not match')


date_pat = re.compile(r'\d+/\d+/\d+')
if date_pat.match(date_text_1):
    print('yes,the date type is match')
else:
    print('no,it is not match')

if date_pat.match(date_text_2):
    print('yes,it match')
else:
    print('no,not match')


date_text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(date_pat.findall(date_text))


date_pat_1 = re.compile(r'(\d+)/(\d+)/(\d+)')


group_result = date_pat_1.match('04/20/2020')
print(f'group result is:{group_result}')
print(f'group 0 is:{group_result.group(0)}')
print(f'group 1 is:{group_result.group(1)}')
print(f'group 2 is:{group_result.group(2)}')
print(f'group 3 is:{group_result.group(3)}')

print(f'groups is:{group_result.groups()}')

month, date, year = group_result.groups()
print(f'month is {month}, date is {date}, year is {year}')

print(date_pat_1.findall(date_text))

for month, day, year in date_pat_1.findall(date_text):
    print(f'{year}-{month}-{day}')


for m_val in date_pat_1.finditer(date_text):
    print(m_val.groups())


group_result = date_pat_1.match('04/20/2020abcdef')
print(group_result)
print(group_result.group())


date_pat_2 = re.compile(r'(\d+)/(\d+)/(\d+)$')
print(date_pat_2.match('04/20/2020abcdef'))
print(date_pat_2.match('04/20/2020'))


print(re.findall(r'(\d+)/(\d+)/(\d+)', date_text))