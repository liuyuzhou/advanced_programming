class A(object):
    def __init__(self, name):
        self.name = name

a = A('attribute')
# print(a.name)
# print(a.test)


class A1(object):
    def __init__(self, name):
        self.name = name

    def __getattr__(self, name):
        print(f'calling __getattr__: {name}')

a = A1('attribute')
# print(a.name)
# print(a.test)


class A2(object):
    def __init__(self, name):
        self.name = name

    def __getattribute__(self, item):
        try:
            return self.__dict__[item]
        except KeyError as es:
            return f'error: {es}'

    def __getattr__(self, name):
        print(f'calling __getattr__: {name}')

a = A2('attribute')
print(a.name)