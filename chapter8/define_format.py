format_dict = {
    'ymd': '{d.year}-{d.month}-{d.day}',
    'mdy': '{d.month}/{d.day}/{d.year}',
    'dmy': '{d.day}/{d.month}/{d.year}'
    }

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, format_type='ymd'):
        """
        :param format_type: 格式化类型，默认使用 ymd 方式
        :return:
        """
        if not format_type:
            format_type = 'ymd'
        fmt = format_dict[format_type]
        return fmt.format(d=self)


curr_data = Date(2020, 5, 6)
print(f'default format: {format(curr_data)}')
print(f"use mdy format: {format(curr_data, 'mdy')}")
print(f'ymd style date is: {curr_data:ymd}')
print(f'mdy style date is: {curr_data:mdy}')


from datetime import date
curr_data = date(2020, 5, 6)
print(f'default format: {format(curr_data)}')
print(f"date info is: {format(curr_data,'%A, %B %d, %Y')}")
print(f'The date is {curr_data:%d %b %Y}')
