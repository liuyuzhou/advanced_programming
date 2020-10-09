from collections import defaultdict

default_dict = defaultdict(list)
default_dict['a'].append(1)
default_dict['b'].append(3)

default_dict = defaultdict(set)
default_dict['a'].add(1)
default_dict['b'].add(2)

d_dict = dict()
d_dict.setdefault('a', []).append(1)
d_dict.setdefault('b', []).append(2)

# 原始手动方式
define_dict = dict()
for key, value in key_value_items:
    if key not in define_dict:
        define_dict[key] = []
    define_dict[key].append(value)

# 改进实现方式
define_dict = defaultdict(list)
for key, value in key_value_items:
    define_dict[key].append(value)