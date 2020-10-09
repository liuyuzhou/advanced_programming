class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return f'Node({self._value})'

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()

if __name__ == '__main__':
    root = Node(0)
    child_1 = Node(1)
    child_2 = Node(2)
    root.add_child(child_1)
    root.add_child(child_2)
    child_1.add_child(Node(3))
    child_1.add_child(Node(4))
    child_2.add_child(Node(5))

    for ch in root.depth_first():
        print(f'child is: {ch}')


class Node2:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return f'Node({self._value})'

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        return DepthFirstIterator(self)


class DepthFirstIterator(object):
    def __init__(self, start_node):
        self._node = start_node
        self._children_iter = None
        self._child_iter = None

    def __iter__(self):
        return self

    def __next__(self):
        # Return myself if just started; create an iterator for children
        if self._children_iter is None:
            self._children_iter = iter(self._node)
            return self._node
        # If processing a child, return its next item
        elif self._child_iter:
            try:
                next_child = next(self._child_iter)
                return next_child
            except StopIteration:
                self._child_iter = None
                return next(self)
        # Advance to the next child and start its iteration
        else:
            self._child_iter = next(self._children_iter).depth_first()
            return next(self)
