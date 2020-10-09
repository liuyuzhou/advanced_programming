record_str = '......##............20 ....#..1513.5 ........##'
total_cost = int(record_str[20:22]) * float(record_str[30:36])
print(f'total cost is:{total_cost}')


NUMBERS = slice(20, 22)
PRICE = slice(30, 36)
total_cost = int(record_str[NUMBERS]) * float(record_str[PRICE])
print(f'total cost is:{total_cost}')

split_obj = slice(3, 20, 2)
print(split_obj.start)
print(split_obj.stop)
print(split_obj.step)

str_obj = 'HelloWorld'
split_obj = slice(3, 20, 2)
for i in range(*split_obj.indices(len(str_obj))):
    print(str_obj[i])