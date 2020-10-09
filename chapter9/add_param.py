from functools import wraps

def optional_debug(func):
    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print('Calling', func.__name__)
        return func(*args, **kwargs)

    return wrapper


@optional_debug
def spam(a, b, c):
    print(f'a = {a}, b = {b}, c = {c}')

spam(1, 2, 3)
spam(1, 2, 3, debug=True)


def a(x, debug=False):
    if debug:
        print('Calling func a')

def b(x, y, z, debug=False):
    if debug:
        print('Calling func b')

def c(x, y, debug=False):
    if debug:
        print('Calling func c')


from functools import wraps
import inspect

def optional_debug(func):
    if 'debug' in inspect.getfullargspec(func):
        raise TypeError('debug argument already defined')

    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print(f'Calling {func.__name__}')
        return func(*args, **kwargs)
    return wrapper

@optional_debug
def a(x):
    pass

@optional_debug
def b(x, y, z):
    pass

@optional_debug
def c(x, y):
    pass


@optional_debug
def add(x,y):
    return x+y

import inspect
print(f'inspect signature: {inspect.signature(add)}')


from functools import wraps
import inspect

def optional_debug(func):
    if 'debug' in inspect.getfullargspec(func):
        raise TypeError('debug argument already defined')

    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print(f'Calling {func.__name__}')
        return func(*args, **kwargs)

    sig = inspect.signature(func)
    parms = list(sig.parameters.values())
    parms.append(inspect.Parameter('debug',
                inspect.Parameter.KEYWORD_ONLY,
                default=False))
    wrapper.__signature__ = sig.replace(parameters=parms)
    return wrapper


@optional_debug
def add(x,y):
    return x+y

print(f'signature: {inspect.signature(add)}')
print(f'add result: {add(5,3)}')