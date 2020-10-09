from inspect import Signature, Parameter
parm_list = [Parameter('x', Parameter.POSITIONAL_OR_KEYWORD),
             Parameter('y', Parameter.POSITIONAL_OR_KEYWORD, default=42),
             Parameter('z', Parameter.KEYWORD_ONLY, default=None)]
sig = Signature(parm_list)
print(f'sig is: {sig}')


def func(*args, **kwargs):
    bound_values = sig.bind(*args, **kwargs)
    for name, value in bound_values.arguments.items():
        print(f'name is: {name}, value is: {value}')

func(1, 2, z=3)
func(1)
func(1, z=3)
func(y=2, x=1)
# func(1, 2, 3, 4)
# func(y=2)
# func(1, y=2, x=3)


from inspect import Signature, Parameter

def make_sig(*names):
    parm_list = [Parameter(name, Parameter.POSITIONAL_OR_KEYWORD)
            for name in names]
    return Signature(parm_list)

class Structure:
    __signature__ = make_sig()
    def __init__(self, *args, **kwargs):
        bound_values = self.__signature__.bind(*args, **kwargs)
        for name, value in bound_values.arguments.items():
            setattr(self, name, value)

class Course(Structure):
    __signature__ = make_sig('course_name', 'total_class', 'score')

class Point(Structure):
    __signature__ = make_sig('x', 'y')


import inspect
print(f'Course signature: {inspect.signature(Course)}')
course_1 = Course('python', 30, 0.3)
# course_2 = Course('python', 30)
# course_3 = Course('python', 30, 0.3, total_class=30)


from inspect import Signature, Parameter

def make_sig(*names):
    parms = [Parameter(name, Parameter.POSITIONAL_OR_KEYWORD)
            for name in names]
    return Signature(parms)

class StructureMeta(type):
    def __new__(cls, cls_name, bases, cls_dict):
        cls_dict['__signature__'] = make_sig(*cls_dict.get('_fields',[]))
        return super().__new__(cls, cls_name, bases, cls_dict)

class Structure(metaclass=StructureMeta):
    _fields = []
    def __init__(self, *args, **kwargs):
        bound_values = self.__signature__.bind(*args, **kwargs)
        for name, value in bound_values.arguments.items():
            setattr(self, name, value)

class Course(Structure):
    _fields = ['course_name', 'total_class', 'score']

class Point(Structure):
    _fields = ['x', 'y']


import inspect
print(f'course signature: {inspect.signature(Course)}')
print(f'point signature: {inspect.signature(Point)}')