from collections import OrderedDict

# A set of descriptors for various types
class Typed:
    _expected_type = type(None)
    def __init__(self, name=None):
        self._name = name

    def __set__(self, instance, value):
        if not isinstance(value, self._expected_type):
            raise TypeError(f'Expected {str(self._expected_type)}')
        instance.__dict__[self._name] = value

class Integer(Typed):
    _expected_type = int

class Float(Typed):
    _expected_type = float

class String(Typed):
    _expected_type = str

# Metaclass that uses an OrderedDict for class body
class OrderedMeta(type):
    def __new__(cls, cls_name, bases, cls_dict):
        d = dict(cls_dict)
        order = []
        for name, value in cls_dict.items():
            if isinstance(value, Typed):
                value._name = name
                order.append(name)
        d['_order'] = order
        return type.__new__(cls, cls_name, bases, d)

    @classmethod
    def __prepare__(cls, cls_name, bases):
        return OrderedDict()


class Structure(metaclass=OrderedMeta):
    def as_csv(self):
        return ','.join(str(getattr(self,name)) for name in self._order)

# Example use
class Course(Structure):
    course_name = String()
    total_class = Integer()
    score = Float()

    def __init__(self, course_name, total_class, score):
        self.course_name = course_name
        self.total_class = total_class
        self.score = score


course = Course('python', 30, 0.3)
print(f'course name: {course.course_name}')
print(f'course as csv: {course.as_csv()}')
# err_ = Course('python','total class', 0.3)


from collections import OrderedDict

class NoDupOrderedDict(OrderedDict):
    def __init__(self, cls_name):
        self.cls_name = cls_name
        super().__init__()
    def __setitem__(self, name, value):
        if name in self:
            raise TypeError(f'{name} already defined in {self.cls_name}')
        super().__setitem__(name, value)

class OrderedMeta(type):
    def __new__(cls, cls_name, bases, cls_dict):
        d = dict(cls_dict)
        d['_order'] = [name for name in cls_dict if name[0] != '_']
        return type.__new__(cls, cls_name, bases, d)

    @classmethod
    def __prepare__(cls, cls_name, bases):
        return NoDupOrderedDict(cls_name)


# class A(metaclass=OrderedMeta):
#     def spam(self):
#         pass
#
#     def spam(self):
#         pass
