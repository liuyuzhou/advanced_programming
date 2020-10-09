import types
from functools import wraps

class Profiled:
    def __init__(self, func):
        wraps(func)(self)
        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)


@Profiled
def add(x, y):
    return x + y

class Spam:
    @Profiled
    def bar(self, x):
        print(f'object: {self}, param is: {x}')


print(f'number add result: {add(3, 5)}')
print(f'number add result: {add(5, 8)}')
print(f'ncalls: {add.ncalls}')

s = Spam()
s.bar(1)
s.bar(2)
s.bar(3)
print(f'bar ncalls: {Spam.bar.ncalls}')


s = Spam()
s.bar(3)


s = Spam()
def grok(self, x):
    pass

print(f'grok get: {grok.__get__(s, Spam)}')


import types
from functools import wraps

def profiled(func):
    ncalls = 0
    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal ncalls
        ncalls += 1
        return func(*args, **kwargs)
    wrapper.ncalls = lambda: ncalls
    return wrapper

# Example
@profiled
def add(x, y):
    return x + y


print(f'number add result: {add(3, 5)}')
print(f'number add result: {add(5, 8)}')
print(f'ncalls: {add.ncalls()}')
