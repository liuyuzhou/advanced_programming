# Base class. Uses a descriptor to set a value
class Descriptor:
    def __init__(self, name=None, **opts):
        self.name = name
        for key, value in opts.items():
            setattr(self, key, value)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

# Descriptor for enforcing types
class Typed(Descriptor):
    expected_type = type(None)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f'expected {str(self.expected_type)}')
        super().__set__(instance, value)

# Descriptor for enforcing values
class Unsigned(Descriptor):
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Expected >= 0')
        super().__set__(instance, value)

class MaxSized(Descriptor):
    def __init__(self, name=None, **opts):
        if 'size' not in opts:
            raise TypeError('missing size option')
        super().__init__(name, **opts)

    def __set__(self, instance, value):
        if len(value) >= self.size:
            raise ValueError(f'size must be < {str(self.size)}')
        super().__set__(instance, value)


class Integer(Typed):
    expected_type = int

class UnsignedInteger(Integer, Unsigned):
    pass

class Float(Typed):
    expected_type = float

class UnsignedFloat(Float, Unsigned):
    pass

class String(Typed):
    expected_type = str

class SizedString(String, MaxSized):
    pass


class Course:
    # Specify constraints
    course_name = SizedString('course_name', size=8)
    total_class = UnsignedInteger('total_class')
    score = UnsignedFloat('score')

    def __init__(self, course_name, total_class, score):
        self.course_name = course_name
        self.total_class = total_class
        self.score = score


course = Course('python', 30, 0.3)
# print(f'course name is: {course.course_name}')
# print(f'total class is: {course.total_class}')
# course.total_class = 20
# print(f'after change,total class is: {course.total_class}')
# course.course_name = 'go'
# print(f'after change,course name is: {course.course_name}')
# course.total_class = -10
course.score = 'hello'


# Class decorator to apply constraints
def check_attributes(**kwargs):
    def decorate(cls):
        for key, value in kwargs.items():
            if isinstance(value, Descriptor):
                value.name = key
                setattr(cls, key, value)
            else:
                setattr(cls, key, value(key))
        return cls

    return decorate

# Example
@check_attributes(course_name=SizedString(size=8),
                  total_class=UnsignedInteger,
                  score=UnsignedFloat)
class Course:
    def __init__(self, course_name, total_class, score):
        self.course_name = course_name
        self.total_class = total_class
        self.score = score


# A metaclass that applies checking
class CheckedMeta(type):
    def __new__(cls, cls_name, bases, methods):
        # Attach attribute names to the descriptors
        for key, value in methods.items():
            if isinstance(value, Descriptor):
                value.name = key
        return type.__new__(cls, cls_name, bases, methods)

# Example
class Course2(metaclass=CheckedMeta):
    course_name = SizedString(size=8)
    total_class = UnsignedInteger()
    score = UnsignedFloat()

    def __init__(self, course_name, total_class, score):
        self.course_name = course_name
        self.total_class = total_class
        self.score = score


# Normal
class Point:
    x = Integer('x')
    y = Integer('y')

# Metaclass
class Point(metaclass=CheckedMeta):
    x = Integer()
    y = Integer()


# Decorator for applying type checking
def typed(expected_type, cls=None):
    if cls is None:
        return lambda cls: Typed(expected_type, cls)
    super_set = cls.__set__

    def __set__(self, instance, value):
        if not isinstance(value, expected_type):
            raise TypeError(f'expected {str(expected_type)}')
        super_set(self, instance, value)

    cls.__set__ = __set__
    return cls

# Decorator for unsigned values
def unsigned(cls):
    super_set = cls.__set__

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Expected >= 0')
        super_set(self, instance, value)

    cls.__set__ = __set__
    return cls

# Decorator for allowing sized values
def max_sized(cls):
    super_init = cls.__init__

    def __init__(self, name=None, **opts):
        if 'size' not in opts:
            raise TypeError('missing size option')
        super_init(self, name, **opts)

    cls.__init__ = __init__

    super_set = cls.__set__

    def __set__(self, instance, value):
        if len(value) >= self.size:
            raise ValueError(f'size must be < {str(self.size)}')
        super_set(self, instance, value)

    cls.__set__ = __set__
    return cls

# Specialized descriptors
@typed(int)
class Integer(Descriptor):
    pass

@unsigned
class UnsignedInteger(Integer):
    pass

@typed(float)
class Float(Descriptor):
    pass

@unsigned
class UnsignedFloat(Float):
    pass

@typed(str)
class String(Descriptor):
    pass

@max_sized
class SizedString(String):
    pass
