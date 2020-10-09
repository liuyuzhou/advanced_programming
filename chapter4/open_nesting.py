from collections import Iterable

def flatten(item_list, ignore_types=(str, bytes)):
    for item in item_list:
        if isinstance(item, Iterable) and not isinstance(item, ignore_types):
            yield from flatten(item)
        else:
            yield item

num_list = [1, 2, [3, 4, [5, 6], 7], 8]
for x in flatten(num_list):
    print(f'number flatten: {x}')


lan_list = ['python', 'java', ['c', 'c++']]
for x in flatten(lan_list):
    print(f'language flatten: {x}')


def flatten(item_list, ignore_types=(str, bytes)):
    for item in item_list:
        if isinstance(item, Iterable) and not isinstance(item, ignore_types):
            for i in flatten(item):
                yield i
        else:
            yield item