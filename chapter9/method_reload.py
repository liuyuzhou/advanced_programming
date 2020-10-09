class Spam:
    def bar(self, x:int, y:int):
        print(f'Bar 1:{x} {y}')

    def bar(self, s:str, n:int = 0):
        print(f'Bar 2: {s} {n}')

s = Spam()
s.bar(5, 8)
s.bar('hello')


import inspect
import types

class MultiMethod:
    """
    Represents a single multimethod.
    """
    def __init__(self, name):
        self._methods = {}
        self.__name__ = name

    def register(self, meth):
        """
        Register a new method as a multimethod
        :param meth:
        :return:
        """
        sig = inspect.signature(meth)

        # Build a type signature from the method's annotations
        types = []
        for name, parm in sig.parameters.items():
            if name == 'self':
                continue
            if parm.annotation is inspect.Parameter.empty:
                raise TypeError(f'Argument {name} must be annotated with a type')
            if not isinstance(parm.annotation, type):
                raise TypeError('Argument {name} annotation must be a type')
            if parm.default is not inspect.Parameter.empty:
                self._methods[tuple(types)] = meth
            types.append(parm.annotation)

        self._methods[tuple(types)] = meth

    def __call__(self, *args):
        """
        Call a method based on type signature of the arguments
        :param args:
        :return:
        """
        types = tuple(type(arg) for arg in args[1:])
        # meth = self._methods.get(types, None)
        if (meth := self._methods.get(types, None)):
            return meth(*args)
        else:
            raise TypeError(f'No matching method for types {types}')

    def __get__(self, instance, cls):
        """
        Descriptor method needed to make calls work in a class
        :param instance:
        :param cls:
        :return:
        """
        if instance is not None:
            return types.MethodType(self, instance)
        else:
            return self

class MultiDict(dict):
    """
    Special dictionary to build multimethods in a metaclass
    """
    def __setitem__(self, key, value):
        if key in self:
            # If key already exists, it must be a multimethod or callable
            current_value = self[key]
            if isinstance(current_value, MultiMethod):
                current_value.register(value)
            else:
                mvalue = MultiMethod(key)
                mvalue.register(current_value)
                mvalue.register(value)
                super().__setitem__(key, mvalue)
        else:
            super().__setitem__(key, value)

class MultipleMeta(type):
    """
    Metaclass that allows multiple dispatch of methods
    """
    def __new__(cls, cls_name, bases, cls_dict):
        return type.__new__(cls, cls_name, bases, dict(cls_dict))

    @classmethod
    def __prepare__(cls, cls_name, bases):
        return MultiDict()


class Spam(metaclass=MultipleMeta):
    def bar(self, x:int, y:int):
        print(f'Bar 1: {x} {y}')

    def bar(self, s:str, n:int = 0):
        print(f'Bar 2: {s} {n}')

# Example: overloaded __init__
import time

class Date(metaclass=MultipleMeta):
    def __init__(self, year: int, month:int, day:int):
        self.year = year
        self.month = month
        self.day = day

    def __init__(self):
        t = time.localtime()
        self.__init__(t.tm_year, t.tm_mon, t.tm_mday)


s = Spam()
s.bar(3, 5)
s.bar('hello world!')
s.bar('hello', 8)
# s.bar(3, 'hello')

e = Date()
print(f'year is: {e.year}')
print(f'month is: {e.month}')
print(f'day is: {e.day}')


b = s.bar
print(f'object b is: {b}')
print(f'self of b is: {b.__self__}')
print(f'func of b is: {b.__func__}')
b(3, 5)
b('hello world!')


# s.bar(x=3, y=5)
# s.bar(s='python')


class A:
    pass

class B(A):
    pass

class C:
    pass

class Spam(metaclass=MultipleMeta):
    def foo(self, x:A):
        print(f'Foo 1: {x}')

    def foo(self, x:C):
        print(f'Foo 2: {x}')


s = Spam()
a = A()
s.foo(a)
c = C()
s.foo(c)
b = B()
# s.foo(b)


import types

class MultiMethod1:
    def __init__(self, func):
        self._methods = {}
        self.__name__ = func.__name__
        self._default = func

    def match(self, *types):
        def register(func):
            ndefaults = len(func.__defaults__) if func.__defaults__ else 0
            for n in range(ndefaults+1):
                self._methods[types[:len(types) - n]] = func
            return self
        return register

    def __call__(self, *args):
        types = tuple(type(arg) for arg in args[1:])
        # meth = self._methods.get(types, None)
        if (meth := self._methods.get(types, None)):
            return meth(*args)
        else:
            return self._default(*args)

    def __get__(self, instance, cls):
        if instance is not None:
            return types.MethodType(self, instance)
        else:
            return self


class Spam:
    @MultiMethod1
    def bar(self, *args):
        # Default method called if no match
        raise TypeError('No matching method for bar')

    @bar.match(int, int)
    def bar(self, x, y):
        print(f'Bar 1: {x} {y}')

    @bar.match(str, int)
    def bar(self, s, n = 0):
        print(f'Bar 2: {s} {n}')
