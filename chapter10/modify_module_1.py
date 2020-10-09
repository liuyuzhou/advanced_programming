from functools import wraps
from chapter10.modify_module import imported_action

def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Calling {func.__name__},args: {args},kwargs: {kwargs}')
        return func(*args, **kwargs)
    return wrapper

@imported_action('math')
def add_logging(mod):
    mod.cos = logged(mod.cos)
    mod.sin = logged(mod.sin)


import math
print(f'math.sin(2) = {math.sin(2)}')