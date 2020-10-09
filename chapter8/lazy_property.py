class LazyProperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value


import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @LazyProperty
    def area(self):
        print('Computing area')
        return math.pi * self.radius ** 2

    @LazyProperty
    def perimeter(self):
        print('Computing perimeter')
        return 2 * math.pi * self.radius


circle = Circle(6.0)
print(f'radius = {circle.radius}')
print(f'area = {circle.area}')
print(f'area = {circle.area}')
print(f'perimeter = {circle.perimeter}')
print(f'perimeter = {circle.perimeter}')


circle = Circle(5.0)
print(f'vars result: {vars(circle)}')
print(f'area = {circle.area}')
print(f'vars result: {vars(circle)}')
print(f'area = {circle.area}')
del circle.area
print(f'vars result: {vars(circle)}')
print(f'area = {circle.area}')


print(f'primary area = {circle.area}')
circle.area = 50
print(f'after modify,area = {circle.area}')


def lazy_property(func):
    name = '_lazy_' + func.__name__
    @property
    def lazy(self):
        if hasattr(self, name):
            return getattr(self, name)
        else:
            value = func(self)
            setattr(self, name, value)
            return value
    return lazy

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @lazy_property
    def area(self):
        print('Computing area')
        return math.pi * self.radius ** 2

    @lazy_property
    def perimeter(self):
        print('Computing perimeter')
        return 2 * math.pi * self.radius


circle = Circle(6.0)
print(f'area = {circle.area}')
circle.area = 50