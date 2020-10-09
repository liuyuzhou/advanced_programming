import weakref

class Node:
    def __init__(self, value):
        self.value = value
        self._parent = None
        self.children = []

    def __repr__(self):
        return f'Node({self.value!r:})'

    # property that manages the parent as a weak-reference
    @property
    def parent(self):
        return None if self._parent is None else self._parent()

    @parent.setter
    def parent(self, node):
        self._parent = weakref.ref(node)

    def add_child(self, child):
        self.children.append(child)
        child.parent = self


root = Node('parent')
c1 = Node('child')
root.add_child(c1)
print(f'c1 parent is: {c1.parent}')
del root
print(f'c1 parent is: {c1.parent}')


# Class just to illustrate when deletion occurs
class Data:
    def __del__(self):
        print('execute Data.__del__')

# Node class involving a cycle
class Node:
    def __init__(self):
        self.data = Data()
        self.parent = None
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        child.parent = self


a = Data()
del a # Immediately deleted
a = Node()
del a # Immediately deleted
a = Node()
a.add_child(Node())
del a # Not deleted (no message)


import gc
print(f'gc.collect() = {gc.collect()}')


# Node class involving a cycle
class Node:
    def __init__(self):
        self.data = Data()
        self.parent = None
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    # NEVER DEFINE LIKE THIS.
    # Only here to illustrate pathological behavior
    def __del__(self):
        del self.data
        del self.parent
        del self.children


a = Node()
a.add_child(Node())
del a
import gc
print(f'gc.collect() = {gc.collect()}')


import weakref
a = Node()
a_ref = weakref.ref(a)
print(f'a ref = {a_ref}')


print(f'a ref = {a_ref()}')
del a
print(f'a ref = {a_ref()}')
