import time
from functools import wraps

# A simple decorator
def time_use(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        print(f'time use: {end - start} s')
        return r
    return wrapper

# Class illustrating application of the decorator to different kinds of methods
class Spam:
    @time_use
    def instance_method(self, n):
        print(f'object: {self}, param: {n}')
        while n > 0:
            n -= 1

    @classmethod
    @time_use
    def class_method(cls, n):
        print(f'object: {cls}, param: {n}')
        while n > 0:
            n -= 1

    @staticmethod
    @time_use
    def static_method(n):
        print(f'param is: {n}')
        while n > 0:
            n -= 1


s = Spam()
s.instance_method(1000000)
Spam.class_method(1000000)
Spam.static_method(1000000)


class Spam:
    @time_use
    @staticmethod
    def static_method(n):
        print(f'param is: {n}')
        while n > 0:
            n -= 1


Spam.static_method(1000000)


from abc import ABCMeta, abstractmethod
class A(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def method(cls):
        pass
