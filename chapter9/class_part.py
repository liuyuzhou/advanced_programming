from functools import wraps

class A:
    # Decorator as an instance method
    def decorator_1(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 1')
            return func(*args, **kwargs)
        return wrapper

    # Decorator as a class method
    @classmethod
    def decorator_2(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 2')
            return func(*args, **kwargs)
        return wrapper


# As an instance method
a = A()
@a.decorator_1
def spam():
    pass
# As a class method
@A.decorator_2
def grok():
    pass


class Person:
    # Create a property instance
    first_name = property()

    # Apply decorator methods
    @first_name.getter
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

person = Person()
person.first_name = 'Bill'
print(f'person first name: {person.first_name}')
person.first_name = 5


class B(A):
    @A.decorator_2
    def bar(self):
        pass