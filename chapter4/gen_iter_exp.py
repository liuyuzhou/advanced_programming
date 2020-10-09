def float_range(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


for n in float_range(0, 2, 0.5):
    print(f'float value is: {n}')

print(list(float_range(0, 2, 0.25)))


def count_down(num):
    print(f'Starting to count from {num}')
    while num > 0:
        yield num
        num -= 1
    print('Done!')

c_obj = count_down(3)
print(f'c obj is: {c_obj}')
print(f'c obj next is: {next(c_obj)}')
print(f'c obj next is: {next(c_obj)}')
print(f'c obj next is: {next(c_obj)}')
print(f'c obj next is: {next(c_obj)}')