class A:
    def spam(self):
        print('This is A.spam')

class B(A):
    def spam(self):
        print('This is B.spam')
        super().spam()  # Call parent spam()


class A:
    def __init__(self):
        self.x = 0

class B(A):
    def __init__(self):
        super().__init__()
        self.y = 1


class Proxy:
    def __init__(self, obj):
        self._obj = obj

    # Delegate attribute lookup to internal obj
    def __getattr__(self, name):
        return getattr(self._obj, name)

    # Delegate attribute assignment
    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value) # Call original __setattr__
        else:
            setattr(self._obj, name, value)


class Base:
    def __init__(self):
        print('call Base.__init__')

class A(Base):
    def __init__(self):
        Base.__init__(self)
        print('call A.__init__')


class Base:
    def __init__(self):
        print('call Base.__init__')

class A(Base):
    def __init__(self):
        Base.__init__(self)
        print('call A.__init__')

class B(Base):
    def __init__(self):
        Base.__init__(self)
        print('call B.__init__')

class C(A,B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print('call C.__init__')


c = C()
print('---------')


class Base:
    def __init__(self):
        print('call Base.__init__')

class A(Base):
    def __init__(self):
        super().__init__()
        print('call A.__init__')

class B(Base):
    def __init__(self):
        super().__init__()
        print('call B.__init__')

class C(A,B):
    def __init__(self):
        super().__init__()  # Only one call to super() here
        print('call C.__init__')


c = C()


print(f'C mro: {C.__mro__}')


class A:
    def spam(self):
        print('This is A.spam')
        super().spam()


# a = A()
# a.spam()


class B:
    def spam(self):
        print('This is B.spam')

class C(A, B):
    pass

c = C()
c.spam()


print(f'C mro: {C.__mro__}')