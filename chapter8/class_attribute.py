# Descriptor attribute for an integer type-checked attribute
class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if not instance:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int object')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Point:
    x = Integer('x')
    y = Integer('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


point = Point(3, 5)
print(f'point x = {point.x}')
print(f'point y = {point.y}')
point.y = 6
print(f'after change,point y = {point.y}')
# point.x = 3.1


# Does NOT work
class Point:
    def __init__(self, x, y):
        # Not work! Must be a class variable
        self.x = Integer('x')
        self.y = Integer('y')
        self.x = x
        self.y = y


# Descriptor attribute for an integer type-checked attribute
class Integer:
    def __get__(self, instance, cls):
        if not instance:
            return self
        else:
            return instance.__dict__[self.name]


point = Point(3, 5)
print(f'attribute x = {point.x}')
print(f'class object Point x = {Point.x}')


# Descriptor for a type-checked attribute
class Typed:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def __get__(self, instance, cls):
        if not instance:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f'Expected {str(self.expected_type)}')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]

# Class decorator that applies it to selected attributes
def typeassert(**kwargs):
    def decorate(cls):
        for name, expected_type in kwargs.items():
            # Attach a Typed descriptor to the class
            setattr(cls, name, Typed(name, expected_type))
        return cls
    return decorate

@typeassert(course_name=str, total_class=int, score=float)
class Stock:
    def __init__(self, course_name, total_class, score):
        self.course_name = course_name
        self.total_class = total_class
        self.score = score
