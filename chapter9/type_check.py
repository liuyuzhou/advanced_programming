from inspect import signature
from functools import wraps

def type_assert(*ty_args, **ty_kwargs):
    def decorate(func):
        # If in optimized mode, disable type checking
        if not __debug__:
            return func

        # Map function argument names to supplied types
        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            # Enforce type assertions across supplied arguments
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError(f'Argument {name} must be {bound_types[name]}')
            return func(*args, **kwargs)
        return wrapper
    return decorate


@type_assert(int, int)
def add(x, y):
    return x + y

print(f'add result: {add(2, 3)}')
# add(2, 'hello')


@type_assert(int, z=int)
def spam(x, y, z=42):
    print(f'x = {x}, y = {y}, z = {z}')

spam(1, 2, 3)
spam(1, 'hello', 3)
# spam(1, 'hello', 'world')


def decorate(func):
    # If in optimized mode, disable type checking
    if not __debug__:
        return func


from inspect import signature
def spam(x, y, z=42):
    pass

sig = signature(spam)
print(f'sig = {sig}')
print(f'parameters: {sig.parameters}')
print(f'parameters z name = {sig.parameters["z"].name}')
print(f'parameters z default = {sig.parameters["z"].default}')
print(f'parameters z kind = {sig.parameters["z"].kind}')


bound_types = sig.bind_partial(int, z=int)
print(f'bound_types = {bound_types}')
print(f'bound_types arguments = {bound_types.arguments}')


bound_values = sig.bind(1, 2, 3)
print(f'arguments = {bound_values.arguments}')


for name, value in bound_values.arguments.items():
    if name in bound_types.arguments:
        if not isinstance(value, bound_types.arguments[name]):
            raise TypeError


@type_assert(int, list)
def bar(x, items=None):
    if items is None:
        items = []
    items.append(x)
    return items
print(f'bar single param: {bar(3)}')
# print(f'bar double param: {bar(3, 5)}')
print(f'bar mix param: {bar(4, [1, 2, 3])}')


@type_assert
def spam(x:int, y, z:int = 42):
    print(x,y,z)
