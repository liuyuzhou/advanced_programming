class MyMeta(type):
    def __new__(cls, cls_name, bases, cls_dict):
        # cls_name is name of class being defined
        # bases is tuple of base classes
        # cls_dict is class dictionary
        return super().__new__(cls, cls_name, bases, cls_dict)


class MyMeta(type):
    def __init__(self, cls_name, bases, cls_dict):
        super().__init__(cls_name, bases, cls_dict)
        # cls_name is name of class being defined
        # bases is tuple of base classes
        # cls_dict is class dictionary


class Root(metaclass=MyMeta):
    pass

class A(Root):
    pass

class B(Root):
    pass


class NoMixedCaseMeta(type):
    def __new__(cls, cls_name, bases, cls_dict):
        for name in cls_dict:
            if name.lower() != name:
                raise TypeError('Bad attribute name: ' + name)
        return super().__new__(cls, cls_name, bases, cls_dict)

class Root(metaclass=NoMixedCaseMeta):
    pass

class A(Root):
    def foo_bar(self):
        pass

class B(Root):
    def fooBar(self):
        pass


from inspect import signature
import logging

class MatchSignaturesMeta(type):

    def __init__(self, cls_name, bases, cls_dict):
        super().__init__(cls_name, bases, cls_dict)
        sup = super(self, self)
        for name, value in cls_dict.items():
            if name.startswith('_') or not callable(value):
                continue
            # Get the previous definition (if any) and compare the signatures
            # prev_dfn = getattr(sup,name,None)
            if (prev_dfn := getattr(sup,name,None)):
                prev_sig = signature(prev_dfn)
                val_sig = signature(value)
                if prev_sig != val_sig:
                    logging.warning(f'Signature mismatch in {value.__qualname__}. {prev_sig} != {val_sig}')

# Example
class Root(metaclass=MatchSignaturesMeta):
    pass

class A(Root):
    def foo(self, x, y):
        pass

    def spam(self, x, *, z):
        pass

# Class with redefined methods, but slightly different signatures
class B(A):
    def foo(self, a, b):
        pass

    def spam(self,x,z):
        pass
