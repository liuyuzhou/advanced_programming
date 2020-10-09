from abc import ABCMeta, abstractmethod

class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, max_bytes=-1):
        pass

    @abstractmethod
    def write(self, data):
        pass


a = IStream()


class SocketStream(IStream):
    def read(self, max_bytes=-1):
        pass

    def write(self, data):
        pass


def serialize(obj, stream):
    if not isinstance(stream, IStream):
        raise TypeError('Expected an IStream')
    pass


import io

# Register the built-in I/O classes as supporting our interface
IStream.register(io.IOBase)

# Open a normal file and type check
# f = open('test.txt')
# print(f'f object is IStream type: {isinstance(f, IStream)}')


class A(metaclass=ABCMeta):
    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, value):
        pass

    @classmethod
    @abstractmethod
    def method_1(cls):
        pass

    @staticmethod
    @abstractmethod
    def method_2():
        pass


# import collections
#
# # Check if x is a sequence
# if isinstance(x, collections.Sequence):
#     pass
#
# # Check if x is iterable
# if isinstance(x, collections.Iterable):
#     pass
#
# # Check if x has a size
# if isinstance(x, collections.Sized):
#     pass
#
# # Check if x is a mapping
# if isinstance(x, collections.Mapping):
#     pass