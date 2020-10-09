exp_list = [1, 4, -5, 10, -7, 2, 3, -1]
print([n for n in exp_list if n > 0])
print([n for n in exp_list if n < 0])


pos_items = (n for n in exp_list if n > 0)
for item in pos_items:
    print(item)


val_list = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False
new_val_list = list(filter(is_int, val_list))
print(new_val_list)


import math
print([math.sqrt(n) for n in exp_list if n > 0])


print([n if n > 0 else 0 for n in exp_list])
print([n if n < 0 else 0 for n in exp_list])



done_work = [
    'read book',
    'running',
    'work',
    'basketball',
    'table tennis',
    'bike',
    'read 20 pages',
    'running 5km',
]
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]


from itertools import compress
more5 = [n > 5 for n in counts]
print(more5)
print(list(compress(done_work, more5)))