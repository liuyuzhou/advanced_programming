xpt_list = [21, 35, 6, 28, 37, 19]
ypt_list = [11, 8, 3, 5, 2, 9]
for x, y in zip(xpt_list, ypt_list):
    print(f'xpt_list element: {x}, ypt_list element: {y}')


a_list = [3, 7, 11]
b_list = ['hello', 'world', 'python', 'good']
for i in zip(a_list, b_list):
    print(f'zip result: {i}')


from itertools import zip_longest
for i in zip_longest(a_list, b_list):
    print(f'zip longest result: {i}')

for i in zip_longest(a_list, b_list, fillvalue=0):
    print(f'zip longest fill value 0: {i}')


header_list = ['name', 'course', 'score']
value_list = ['python', 20, 0.3]


s = dict(zip(header_list, value_list))


for name, val in zip(header_list, value_list):
    print(f'{name} = {val}')


a_list = [1, 2, 3]
b_list = [10, 11, 12]
c_list = ['x','y','z']
for i in zip(a_list, b_list, c_list):
    print(f'zip result: {i}')


print(f'zip {a_list} {b_list} = {zip(a_list, b_list)}')
print(f'list zip result: {list(zip(a_list, b_list))}')