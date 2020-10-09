add = lambda x, y: x + y
print(f'number add result = {add(2, 3)}')

print(f"str add result: {add('hello', 'world')}")


def add(x, y):
    return x + y

print(f'add function: {add(2, 3)}')


name_list = ['python', 'java', 'go', 'c++']
print(f'sorted result: {sorted(name_list, key=lambda name: name.split()[-1].lower())}')