# Methods
def __init__(self, course_name, total_class, score):
    self.course_name = course_name
    self.total_class = total_class
    self.score = score

def total_score(self):
    return self.total_class * self.score

cls_dict = {
    '__init__' : __init__,
    'total_score' : total_score,
}

# Make a class
import types

Course = types.new_class('Course', (), {}, lambda ns: ns.update(cls_dict))
Course.__module__ = __name__


course = Course('python', 30, 0.3)
print(f'course object is: {course}')
print(f'total score = {course.total_score()}')


import abc
Course = types.new_class('Course', (), {'metaclass': abc.ABCMeta}, lambda ns: ns.update(cls_dict))
Course.__module__ = __name__
print(f'Course object: {Course}')
print(f'Course type: {type(Course)}')


# class Spam(Base, debug=True, typecheck=False):
#     pass
#
#
# Spam = types.new_class('Spam', (Base,), {'debug': True, 'typecheck': False},
#                        lambda ns: ns.update(cls_dict))


import collections
Course = collections.namedtuple('Course', ['course_name', 'total_class', 'score'])
print(f'Course object: {Course}')


import operator
import types
import sys

def named_tuple(class_name, field_names):
    # Populate a dictionary of field property accessors
    cls_dict = {name: property(operator.itemgetter(n)) for n, name in enumerate(field_names)}

    # Make a __new__ function and add to the class dict
    def __new__(cls, *args):
        if len(args) != len(field_names):
            raise TypeError(f'Expected {len(field_names)} arguments')
        return tuple.__new__(cls, args)

    cls_dict['__new__'] = __new__

    # Make the class
    cls = types.new_class(class_name, (tuple,), {}, lambda ns: ns.update(cls_dict))

    # Set the module to that of the caller
    cls.__module__ = sys._getframe(1).f_globals['__name__']
    return cls


Point = named_tuple('Point', ['x', 'y'])
print(f'point object: {Point}')
p = Point(5, 8)
print(f'p length = {len(p)}')
print(f'p.x = {p.x}')
print(f'p.y = {p.y}')
# p.x = 3
print(f'p is: {p}')


Course = type('Course', (), cls_dict)


import types
metaclass, kwargs, ns = types.prepare_class('Course', (), {'metaclass': type})
