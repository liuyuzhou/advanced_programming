class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


d = Date.__new__(Date)
# print(f'data object is: {d}')
print(d.year)


data = {'year': 2020, 'month': 5, 'day': 10}

for key, value in data.items():
    setattr(d, key, value)

# print(f'year is: {d.year}')
# print(f'month is: {d.month}')


from time import localtime

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        d = cls.__new__(cls)
        t = localtime()
        d.year = t.tm_year
        d.month = t.tm_mon
        d.day = t.tm_mday
        return d


data = {'year': 2020, 'month': 5, 'day': 10}