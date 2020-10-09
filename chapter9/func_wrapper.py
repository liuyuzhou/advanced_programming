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
        print(f'func name: {func.__name__}, time use: {end - start} s')
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
count_down(10000000)


@time_use
def count_down(n):
    pass


def count_down(n):
    pass

countdown = time_use(count_down)


class A:
    @classmethod
    def method(cls):
        pass

class B:
    # Equivalent definition of a class method
    def method(cls):
        pass
    method = classmethod(method)