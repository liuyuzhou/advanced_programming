import time
from functools import wraps

def time_this(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        r = func(*args, **kwargs)
        end = time.perf_counter()
        print(f'{func.__module__}.{func.__name__} time spend: {end - start}s')
        return r
    return wrapper


@time_this
def countdown(n):
    while n > 0:
            n -= 1

countdown(10000000)


from contextlib import contextmanager

@contextmanager
def time_block(label):
    start = time.perf_counter()
    try:
        yield
    finally:
        end = time.perf_counter()
        print(f'{label} time spend: {end - start}s')


with time_block('counting'):
    n = 10000000
    while n > 0:
            n -= 1


from timeit import timeit
print(f"math.sqrt time spend: {timeit('math.sqrt(2)', 'import math')}s")
print(f"sqrt time spend: {timeit('sqrt(2)', 'from math import sqrt')}s")


print(f"math.sqrt time spend: {timeit('math.sqrt(2)', 'import math', number=10000000)}s")
print(f"sqrt time spend: {timeit('sqrt(2)', 'from math import sqrt', number=10000000)}s")


from functools import wraps
def time_this(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.process_time()
        r = func(*args, **kwargs)
        end = time.process_time()
        print(f'{func.__module__}.{func.__name__} : {end - start}')
        return r
    return wrapper