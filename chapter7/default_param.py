def default_func(a, b=42):
    print(f'a = {a}, b = {b}')

default_func(1)
default_func(1, 2)


# Using a list as a default value
def default_func(a, b=None):
    if b is None:
        b = []


_no_value = object()

def default_func(a, b=_no_value):
    if b is _no_value:
        print('No b value supplied')
    else:
        print(f'a = {a}, b = {b}')


default_func(1)
default_func(1, 2)
default_func(1, None)


x = 42
def default_func(a, b=x):
    print(f'a = {a}, b = {b}')

default_func(1)

x = 23
default_func(1)


def default_func(a, b=[]): # NO!
    pass


def default_func(a, b=[]):
    print(f'b = {b}')
    return b

x = default_func(1)

x.append(99)
x.append('Yow!')
print(f'x = {x}')
default_func(1)


def default_func(a, b=None):
    if not b:
        b = []
    print(f'a = {a}, b = {b}')


default_func(1)
default_func(1, [])
default_func(1, 0)
default_func(1, '')