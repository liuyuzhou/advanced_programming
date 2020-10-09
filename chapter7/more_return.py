def more_return_func():
    return 1, 2, 3

a, b, c = more_return_func()
print(f'value of a = {a}')
print(f'value of b = {b}')
print(f'value of c = {c}')


a = (1, 2)
print(f'a = {a}')

b = 1, 2
print(f'b = {b}')


print(f'more return: {more_return_func()}')
