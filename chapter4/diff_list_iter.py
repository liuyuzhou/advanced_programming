from itertools import chain
a_list = [1, 3, 5, 7]
b_list = ['hello', 'world', 'nice']
for x in chain(a_list, b_list):
    print(f'chain result: {x}')


active_items = set()
inactive_items = set()

for item in chain(active_items, inactive_items):
    pass


for item in active_items:
    pass

for item in inactive_items:
    pass


# Inefficent
for x in a_list + b_list:
    pass

# Better
for x in chain(a_list, b_list):
    pass