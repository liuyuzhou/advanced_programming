import collections
class A(collections.Iterable):
    pass


a = A()


import collections
collections.Sequence()


import bisect

class SortedItems(collections.Sequence):
    def __init__(self, initial=None):
        self._items = sorted(initial) if initial is not None else []

    # Required sequence methods
    def __getitem__(self, index):
        return self._items[index]

    def __len__(self):
        return len(self._items)

    # Method for adding an item in the right location
    def add(self, item):
        bisect.insort(self._items, item)

item_list = SortedItems([5, 1, 3])
print(f'item list = {list(item_list)}')
print(f'item_list[0] = {item_list[0]}, item_list[-1] = {item_list[-1]}')
item_list.add(2)
print(f'item_list = {list(item_list)}')


item_list = SortedItems()
import collections
print(f'is item_list Iterable: {isinstance(item_list, collections.Iterable)}')
print(f'is item_list Sequence: {isinstance(item_list, collections.Iterable)}')
print(f'is item_list Container: {isinstance(item_list, collections.Iterable)}')
print(f'is item_list Sized: {isinstance(item_list, collections.Iterable)}')
print(f'is item_list Mapping: {isinstance(item_list, collections.Iterable)}')


class Items(collections.MutableSequence):
    def __init__(self, initial=None):
        self._items = list(initial) if initial is not None else []

    # Required sequence methods
    def __getitem__(self, index):
        print(f'Getting: {index}')
        return self._items[index]

    def __setitem__(self, index, value):
        print(f'Setting: {index} {value}')
        self._items[index] = value

    def __delitem__(self, index):
        print(f'Deleting: {index}')
        del self._items[index]

    def insert(self, index, value):
        print(f'Inserting: {index} {value}')
        self._items.insert(index, value)

    def __len__(self):
        print('Calculation object length.')
        return len(self._items)


a_item = Items([1, 2, 3])
print(f'len of a is: {len(a_item)}')

a_item.append(4)
a_item.append(2)
a_item.count(2)
a_item.remove(2)