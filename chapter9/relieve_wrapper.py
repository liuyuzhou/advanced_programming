import time
from functools import wraps

def time_use(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'func name: {func.__name__},time use: {end - start} s')
        return result
    return wrapper

@time_use
def add(x, y):
    return x + y

orig_add = add.__wrapped__
print(f'add result: {orig_add(3, 5)}')


def decorator_1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Call decorator 1')
        return func(*args, **kwargs)
    return wrapper

def decorator_2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Call decorator 2')
        return func(*args, **kwargs)
    return wrapper

@decorator_1
@decorator_2
def add(x, y):
    return x + y


print(f'add result = {add(3, 5)}')
print(f'wrapped add result = {add.__wrapped__(3, 5)}')
