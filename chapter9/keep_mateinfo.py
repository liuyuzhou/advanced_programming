import time
from functools import wraps
def time_use(func):
    """
    Decorator that reports the execution time.
    :param func:
    :return:
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'func name: {func.__name__},time use: {end - start} s')
        return result
    return wrapper


@time_use
def count_down(n):
    """
    Counts down
    :param n:
    :return:
    """
    while n > 0:
        n -= 1

count_down(100000)
print(f'func name: {count_down.__name__}')
print(f'func doc: {count_down.__doc__}')
print(f'func annotations: {count_down.__annotations__}')


def time_use(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'func name: {func.__name__},time use: {end - start} s')
        return result
    return wrapper

@time_use
def count_down(n):
    """
    Counts down
    :param n:
    :return:
    """
    while n > 0:
        n -= 1
print(f'func name: {count_down.__name__}')
print(f'doc is: {count_down.__doc__}')
print(f'annotations is: {count_down.__annotations__}')


print(f'wrapped： {count_down.__wrapped__(100000)}')


from inspect import signature
print(f'signature: {signature(count_down)}')
