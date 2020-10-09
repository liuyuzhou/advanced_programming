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
        print(f'func name is: {func.__name__}, time use: {end - start} s')
        return result
    return wrapper