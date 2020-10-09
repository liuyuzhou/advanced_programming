import operator

class StructTupleMeta(type):
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for n, name in enumerate(cls._fields):
            setattr(cls, name, property(operator.itemgetter(n)))

class StructTuple(tuple, metaclass=StructTupleMeta):
    _fields = []
    def __new__(cls, *args):
        if len(args) != len(cls._fields):
            raise ValueError(f'{len(cls._fields)} arguments required')
        return super().__new__(cls,args)


class Course(StructTuple):
    _fields = ['course_name', 'total_class', 'score']

class Point(StructTuple):
    _fields = ['x', 'y']


course = Course('python', 30, 0.3)
print(f'course is: {course}')
print(f'course[0] = {course[0]}')
print(f'course.course_name = {course.course_name}')
print(f'course total_score = {course.total_class * course.score}')

course.total_class = 20


course = Course('python', 30, 0.3)
# course = Course(('python', 30, 0.3))
