def test_func():
    n = 0
    # Closure function
    def func():
        print(f'var n = {n}')

    # Accessor methods for n
    def get_n():
        return n

    def set_n(value):
        nonlocal n
        n = value

    # Attach as function attributes
    func.get_n = get_n
    func.set_n = set_n
    return func


f = test_func()
f()
f.set_n(10)
f()
print(f'get n is: {f.get_n()}')


import sys
class ClosureInstance(object):
    def __init__(self, locals=None):
        if locals is None:
            locals = sys._getframe(1).f_locals

        # Update instance dictionary with callables
        self.__dict__.update((key,value) for key, value in locals.items()
                            if callable(value) )
    # Redirect special methods
    def __len__(self):
        return self.__dict__['__len__']()

def stack_1():
    items = []
    def push(item):
        items.append(item)

    def pop():
        return items.pop()

    def __len__():
        return len(items)

    return ClosureInstance()


s = stack_1()
print(f's object: {s}')
s.push(10)
s.push(20)
s.push('Hello')
print(f'len of s = {len(s)}')
print(f'pop object: {s.pop()}')
print(f'pop object: {s.pop()}')
print(f'pop object: {s.pop()}')


class StackObj(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def __len__(self):
        return len(self.items)


from timeit import timeit
s = stack_1()
print(f"closure time use: {timeit('s.push(1);s.pop()', 'from __main__ import s')}")
so = StackObj()
print(f"time use: {timeit('so.push(1);so.pop()', 'from __main__ import so')}")