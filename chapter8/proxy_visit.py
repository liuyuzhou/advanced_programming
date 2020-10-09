class A(object):
    def spam(self, x):
        pass

    def foo(self):
        pass

class B(object):
    """
    简单的代理
    """
    def __init__(self):
        self._a = A()

    def spam(self, x):
        # Delegate to the internal self._a instance
        return self._a.spam(x)

    def foo(self):
        # Delegate to the internal self._a instance
        return self._a.foo()

    def bar(self):
        pass


class B2(object):
    """
    使用__getattr__的代理，代理方法比较多时候
    """
    def __init__(self):
        self._a = A()

    def bar(self):
        pass

    # Expose all of the methods defined on class A
    def __getattr__(self, name):
        """
        这个方法在访问的attribute不存在的时候被调用
        the __getattr__() method is actually a fallback method
        that only gets called when an attribute is not found
        :param name:
        :return:
        """
        return getattr(self._a, name)


b = B()
# Calls B.bar() (exists on B)
b.bar()
# Calls B.__getattr__('spam') and delegates to A.spam
b.spam(30)


# A proxy class that wraps around another object, but
# exposes its public attributes
class Proxy(object):
    def __init__(self, obj):
        self._obj = obj

    # Delegate attribute lookup to internal obj
    def __getattr__(self, name):
        print(f'getattr: {name}')
        return getattr(self._obj, name)

    # Delegate attribute assignment
    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            print(f'setattr: {name} {value}')
            setattr(self._obj, name, value)

    # Delegate attribute deletion
    def __delattr__(self, name):
        if name.startswith('_'):
            super().__delattr__(name)
        else:
            print(f'delattr: {name}')
            delattr(self._obj, name)


class Spam(object):
    def __init__(self, x):
        self.x = x

    def bar(self, y):
        print(f'Spam.bar: {self.x}, {y}')

# Create an instance
# s = Spam(2)
# # Create a proxy around it
# p = Proxy(s)
# # Access the proxy
# print(f'p.x = {p.x}')
# p.bar(3)
# p.x = 37


class A(object):
    def spam(self, x):
        print(f'A.spam {x}')
    def foo(self):
        print('A.foo')

class B(A):
    def spam(self, x):
        print('B.spam')
        super().spam(x)
    def bar(self):
        print('B.bar')


class A(object):
    def spam(self, x):
        print(f'A.spam {x}')
    def foo(self):
        print('A.foo')

class B(object):
    def __init__(self):
        self._a = A()
    def spam(self, x):
        print(f'B.spam {x}')
        self._a.spam(x)
    def bar(self):
        print('B.bar')
    def __getattr__(self, name):
        return getattr(self._a, name)


class ListLike(object):
    """__getattr__对于双下划线开始和结尾的方法是不能用的，需要一个个去重定义"""

    def __init__(self):
        self._items = []

    def __getattr__(self, name):
        return getattr(self._items, name)


a = ListLike()
a.append(2)
a.insert(0, 1)
a.sort()
# len(a)
# a[0]


class ListLike(object):
    """__getattr__对于双下划线开始和结尾的方法是不能用的，需要一个个去重定义"""

    def __init__(self):
        self._items = []

    def __getattr__(self, name):
        return getattr(self._items, name)

    # Added special methods to support certain list operations
    def __len__(self):
        return len(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __delitem__(self, index):
        del self._items[index]