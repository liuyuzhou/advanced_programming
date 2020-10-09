import math

class Structure1:
    # Class variable that specifies expected fields
    _field_list = []

    def __init__(self, *args):
        if len(args) != len(self._field_list):
            raise TypeError(f'Expected {len(self._field_list)} arguments')
        # Set the arguments
        for name, value in zip(self._field_list, args):
            setattr(self, name, value)


# Example class definitions
class Course(Structure1):
    _field_list = ['course_name', 'total_class', 'score']

class Point(Structure1):
    _field_list = ['x', 'y']

class Circle(Structure1):
    _field_list = ['radius']

    def area(self):
        return math.pi * self.radius ** 2


course = Course('python', 30, 0.3)
p = Point(2, 3)
c = Circle(4.5)
# course_1 = Course('python', 30)


class Structure2:
    _field_list = []

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._field_list):
            raise TypeError(f'Expected {len(self._field_list)} arguments')

        # Set all of the positional arguments
        for name, value in zip(self._field_list, args):
            setattr(self, name, value)

        # Set the remaining keyword arguments
        for name in self._field_list[len(args):]:
            setattr(self, name, kwargs.pop(name))

        # Check for any remaining unknown arguments
        if kwargs:
            raise TypeError(f"Invalid argument(s): {','.join(kwargs)}")
# Example use
if __name__ == '__main__':
    class Course(Structure2):
        _field_list = ['course_name', 'total_class', 'score']

    course_1 = Course('python', 30, 0.3)
    course_2 = Course('python', 30, score=0.3)
    course_3 = Course('python', total_class=30, score=0.3)
    # course_3 = Course('python', total_class=30, score=0.3, aa=1)


class Structure3:
    # Class variable that specifies expected fields
    _field_list = []

    def __init__(self, *args, **kwargs):
        if len(args) != len(self._field_list):
            raise TypeError(f'Expected {len(self._field_list)} arguments')

        # Set the arguments
        for name, value in zip(self._field_list, args):
            setattr(self, name, value)

        # Set the additional arguments (if any)
        extra_args = kwargs.keys() - self._field_list
        for name in extra_args:
            setattr(self, name, kwargs.pop(name))

        if kwargs:
            raise TypeError(f"Duplicate values for {','.join(kwargs)}")

# Example use
if __name__ == '__main__':
    class Course(Structure3):
        _field_list = ['course_name', 'total_class', 'score']

    course_1 = Course('python', 30, 0.3)
    course_2 = Course('python', 30, 0.3, date='8/5/2020')


class Structure:
    # Class variable that specifies expected fields
    _field_list= []
    def __init__(self, *args):
        if len(args) != len(self._field_list):
            raise TypeError(f'Expected {len(self._field_list)} arguments')

        # Set the arguments (alternate)
        self.__dict__.update(zip(self._field_list,args))


help(Course)
