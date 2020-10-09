@typeassert(int, int)
def add(x, y):
    return x + y

print(f'{add(2, 3)}')
print(f"{add(2, 'hello')}")


from inspect import signature
from functools import wraps

def typeassert(*ty_args, **ty_kwargs):
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
                        raise TypeError(
                            'Argument {} must be {}'.format(name, bound_types[name])
                            )
            return func(*args, **kwargs)
        return wrapper
    return decorate


@typeassert(int, z=int)
def spam(x, y, z=42):
    print(x, y, z)

print(f'{spam(1, 2, 3)}')
print(f"{spam(1, 'hello', 3)}")
print(f"{spam(1, 'hello', 'world')}")


def decorate(func):
    # If in optimized mode, disable type checking
    if not __debug__:
        return func


from inspect import signature
def spam(x, y, z=42):
    pass

sig = signature(spam)
print(sig)
print(f'{sig.parameters}')
print(f"{sig.parameters['z'].name}")
print(f"{sig.parameters['z'].default}")
print(f"{sig.parameters['z'].kind}")


bound_types = sig.bind_partial(int,z=int)
print(f'{bound_types}')
print(f'{bound_types.arguments}')


bound_values = sig.bind(1, 2, 3)
print(f'{bound_values.arguments}')


for name, value in bound_values.arguments.items():
    if name in bound_types.arguments:
        if not isinstance(value, bound_types.arguments[name]):
            raise TypeError


@typeassert(int, list)
def bar(x, items=None):
    if items is None:
        items = []
    items.append(x)
    return items
print(f'{bar(2)}')
print(f'{bar(2, 3)}')
print(f'{bar(4, [1, 2, 3])}')


@typeassert
def spam(x:int, y, z:int = 42):
    print(x, y, z)
